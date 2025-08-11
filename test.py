
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import glob
import google.generativeai as genai

# Load API key directly from .env or environment
import dotenv
dotenv.load_dotenv('config/.env')
API_KEY = os.getenv('GEMINI_API_KEY')
if not API_KEY:
	raise RuntimeError('GEMINI_API_KEY not found in environment or .env file')
genai.configure(api_key=API_KEY)

# Remove any Google Cloud credentials from environment to avoid conflicts
os.environ.pop('GOOGLE_APPLICATION_CREDENTIALS', None)
os.environ.pop('GOOGLE_API_KEY', None)

SOP_PATH = 'data/consolidated/consolidated_documents.txt'
TICKET_DIR = 'data/ticket/ticket_data/'
OUTPUT_BASE = 'outputs/'

def read_file(path):
	with open(path, 'r', encoding='utf-8') as f:
		return f.read()

def get_output_folder(ticket_file):
	base = os.path.basename(ticket_file)
	name, _ = os.path.splitext(base)
	return os.path.join(OUTPUT_BASE, name)

def process_ticket(ticket_path, sop_content, model):
	print(f"Starting processing for: {ticket_path}")
	ticket_content = read_file(ticket_path)
	prompt = f"""
You are an expert at matching tickets to SOPs. Given the following SOP content and ticket, answer:
1. What is the issue mentioned in the ticket?
2. What is the title of the SOP that best solves this ticket?
3. What is the content of that SOP?
4. What steps in the SOP need to be modified to create a tailored solution for this ticket?( mention all the steps
whether they need modification or not)

SOP Content:
{sop_content}

Ticket Content:
{ticket_content}
"""
	response = model.generate_content(prompt)
	result_text = response.text if hasattr(response, 'text') else str(response)

	# Try to parse Gemini response into JSON structure
	import re, json
	def extract_section(pattern, text):
		match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
		return match.group(1).strip() if match else None

	result_json = {
		"ticket_file": os.path.basename(ticket_path),
		"issue": extract_section(r"1\.\s*What is the issue mentioned in the ticket\?\s*(.*?)(?:2\.|$)", result_text),
		"sop_title": extract_section(r"2\.\s*What is the title of the SOP.*?\?\s*(.*?)(?:3\.|$)", result_text),
		"sop_content": extract_section(r"3\.\s*What is the content of that SOP.*?\?\s*(.*?)(?:4\.|$)", result_text),
		"sop_steps_modification": extract_section(r"4\.\s*What steps in the SOP.*?\?\s*(.*)", result_text)
	}

	output_folder = get_output_folder(ticket_path)
	os.makedirs(output_folder, exist_ok=True)
	output_file = os.path.join(output_folder, 'result.json')
	with open(output_file, 'w', encoding='utf-8') as f:
		json.dump(result_json, f, indent=2, ensure_ascii=False)
	print(f"Finished processing: {ticket_path} -> {output_file}")

def main():
	print("Loading SOP and ticket files...")
	sop_content = read_file(SOP_PATH)
	ticket_files = glob.glob(os.path.join(TICKET_DIR, '*.txt'))
	print(f"Found {len(ticket_files)} ticket files.")
	model = genai.GenerativeModel('gemini-2.5-pro', generation_config={"temperature": 0})
	print("Starting parallel ticket processing...")
	with ThreadPoolExecutor() as executor:
		futures = [executor.submit(process_ticket, ticket_path, sop_content, model) for ticket_path in ticket_files]
		for future in as_completed(futures):
			future.result()
	print("All tickets processed.")

if __name__ == '__main__':
	main()
	# All code after this line is removed to clean up the file
	# Everything below this line is duplicate and will be removed
