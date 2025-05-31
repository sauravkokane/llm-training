from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
	path="D:/Python Projects/llm_training/7. document_loaders/data",
	glob="*.pdf",
	loader_cls=PyPDFLoader,
)

doc_no = 0
for doc in loader.lazy_load():
	doc_no += 1
	if not (doc_no%100):
		print(doc.metadata)
output = [
	{
		'producer': 'iLovePDF', 
		'creator': 'PyPDF', 
		'creationdate': '', 
		'moddate': '2024-07-01T11:20:33+00:00', 
		'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
		'total_pages': 402, 
		'page': 52, 
		'page_label': '53'
	},
	{
		'producer': 'iLovePDF', 
		'creator': 'PyPDF', 
		'creationdate': '', 
		'moddate': '2024-07-01T11:20:33+00:00', 
		'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
		'total_pages': 402, 
		'page': 152, 
		'page_label': '153'
	},
	{
		'producer': 'iLovePDF', 
		'creator': 'PyPDF', 
		'creationdate': '', 
		'moddate': '2024-07-01T11:20:33+00:00', 
		'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
		'total_pages': 402, 
		'page': 252, 
		'page_label': '253'
	},
	{
		'producer': 'iLovePDF', 
		'creator': 'PyPDF', 
		'creationdate': '', 
		'moddate': '2024-07-01T11:20:33+00:00', 
		'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
		'total_pages': 402, 
		'page': 352, 
		'page_label': '353'
	},
	{
		'producer': 'iTextSharp™ 5.5.13.1 ©2000-2019 iText Group NV (AGPL-version)', 
		'creator': 'PyPDF', 
		'creationdate': '2023-12-25T21:46:27+05:30', 
		'moddate': '2023-12-25T21:48:28+05:30', 
		'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\Nagarik Suraksha Samhita.pdf', 
		'total_pages': 249, 
		'page': 50, 
		'page_label': '51'
	},
	{
		'producer': 'iTextSharp™ 5.5.13.1 ©2000-2019 iText Group NV (AGPL-version)', 
		'creator': 'PyPDF', 
		'creationdate': '2023-12-25T21:46:27+05:30', 
		'moddate': '2023-12-25T21:48:28+05:30', 
		'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\Nagarik Suraksha Samhita.pdf', 
		'total_pages': 249, 
		'page': 150, 
		'page_label': '151'
	},
	{
		'producer': 'Adobe PDF Library 15.0', 
		'creator': 'Adobe InDesign 14.0 (Macintosh)', 
		'creationdate': '2021-05-26T18:08:45-07:00', 
		'author': 'Al Sweigart', 
		'moddate': '2021-06-03T10:49:31-07:00', 
		'title': 'The Big Book of Small Pythin Projects', 
		'trapped': '/False', 
		'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\The Big Book of Small Python Projects 81 Easy Practice Programs by Al Sweigart (z-lib.org).pdf', 
		'total_pages': 434, 
		'page': 1, 
		'page_label': ''
	},
]