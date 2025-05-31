from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader(
	path="D:/Python Projects/llm_training/7. document_loaders/data",
	glob = "**/[!.]*.pdf",
	# silent_errors = False,
)

doc_no = 0
docs = []
for doc in loader.lazy_load():
	# print(doc)
	doc_no += 1
	if doc_no>=700:
		break
	docs.append(doc)

print(docs[400:405])
# for document in load:
# 	print(document.page_content[:100])
# 	print(document.metadata)

	# 	break


# [
# 	Document(
# 		metadata={
# 			'producer': 'iLovePDF', 
# 			'creator': 'PyPDF', 
# 			'creationdate': '', 
# 			'moddate': '2024-07-01T11:20:33+00:00', 
# 			'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
# 			'total_pages': 402, 
# 			'page': 353, 
# 			'page_label': '354'
# 		}, 
# 		page_content='''THE CONSTITUTION OF  INDIA(Seventh Schedule) 32321. Commercial and industrial monopolies, combines and trusts.22. Trade unions; industrial and labour disputes.23. Social security and social insurance; employment and unemployment.24. Welfare of labour including conditions of work, provident funds, employers' liability, workmen's compensation, invalidity and old age pensions and maternity benefits.1[25. Education, including technical education, medical education and universities, subject to the provisions of entries 63, 64, 65 and 66 of List I; vocational and technical training of labour.]26. Legal, medical and other professions.27. Relief and rehabilitation of persons displaced from their original place of residence by reason of the setting up of the Dominions of India and Pakistan.28. Charities  and  charitable  institutions,  charitable and religious endowments and religious institutions.29. Prevention of the extension from one State to another of infectious or contagious diseases or pests affecting men, animals or plants. 30. Vital statistics including registration of births and deaths.31. Ports other than those declared by or under law made by Parliament or existing law to be major ports.32. Shipping and navigation on inland waterways as regards mechanically propelled vessels, and the rule of the road on such waterways, and the carriage of passengers and goods on inland waterways subject to the provisions of List I with respect to national waterways.2[33. Trade and commerce in, and the production, supply and distribution of,—(a) the products of any industry where the control of such industry by the Union is declared by Parliament by law to be expedient in the public interest, and imported goods of the same kind as such products;(b) foodstuffs, including edible oilseeds and oils;(c) cattle fodder, including oilcakes and other concentrates;(d) raw cotton, whether ginned or unginned, and cotton seed; and(e) raw jute.]______________________________________________1. Subs. by the Constitution (Forty-second Amendment) Act, 1976, s. 57 (w.e.f. 3-1-1977).2. Subs. by the Constitution (Third Amendment) Act, 1954, s. 2 for entry 33             (w.e.f. 22-2-1955).'''
# 	), 
# 	Document(
# 		metadata={
# 			'producer': 'iLovePDF', 
# 			'creator': 'PyPDF', 
# 			'creationdate': '', 
# 			'moddate': '2024-07-01T11:20:33+00:00', 
# 			'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
# 			'total_pages': 402, 
# 			'page': 354, 
# 			'page_label': '355'
# 		}, 
# 		page_content='''THE CONSTITUTION OF  INDIA(Seventh Schedule) 3241[33A. Weights and measures except establishment of standards.]34.  Price control. 35. Mechanically propelled vehicles including the principles on which taxes on such vehicles are to be levied.36. Factories37. Boilers.38. Electricity. 39. Newspapers, books and printing presses. 40. Archaeological sites and remains other than those 2[declared by or under law made by Parliament] to be of national importance.41. Custody, management and disposal of property (including agricultural land) declared by law to be evacuee property. 3[42. Acquisition and requisitioning of property.]43. Recovery in a State of claims in respect of taxes and other public demands, including arrears of land-revenue and sums recoverable as such arrears, arising outside that State.44. Stamp duties other than duties or fees collected by means of judicial stamps, but not including rates of stamp duty.45. Inquiries and statistics for the purposes of any of the matters specified in List II or List III.46. Jurisdiction and powers of all courts, except the Supreme Court, with respect to any of the matters in this List.47. Fees in respect of any of the matters in this List, but not including fees taken in any court.______________________________________________1. Ins. by the Constitution (Forty-second Amendment) Act, 1976, s. 57 (w.e.f. 3-1-1977).2. Subs. by the Constitution (Seventh Amendment) Act, 1956, s. 27, for "declared by Parliament by law" (w.e.f. 1-11-1956).3.  Subs. by s. 26, ibid.for entry 42 (w.e.f. 1-11-1956).'''
# 	), 
# 	Document(
# 		metadata={
# 			'producer': 'iLovePDF', 
# 			'creator': 'PyPDF', 
# 			'creationdate': '', 
# 			'moddate': '2024-07-01T11:20:33+00:00', 
# 			'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
# 			'total_pages': 402, 
# 			'page': 355, 
# 			'page_label': '356'
# 		}, 
# 		page_content='''325
# EIGHTH SCHEDULE[Articles 344(1) and 351]Languages 1.   Assamese.2.   Bengali.1[3.   Bodo. 4.  Dogri.] 2[5.] Gujarati.3[6.] Hindi.3[7.] Kannada.3[8.]  Kashmiri. 4[3[9.]   Konkani.]1[10. Maithili.]5[11.] Malayalam.4[6[12.] Manipuri.]6[13.] Marathi.4[6[14.] Nepali.]6[15.]7[Odia].6[16.] Punjabi.6[17.] Sanskrit.______________________________________________1. Ins. by the Constitution (Ninety-second Amendment) Act, 2003, s. 2 (w.e.f. 7-1-2004).2. Entry 3 renumbered as entry 5 by s. 2, ibid.(w.e.f. 7-1-2004).3. Entries 4 to 7 renumbered as entries 6 to 9 by s. 2, ibid.(w.e.f. 7-1-2004).4. Ins. by the Constitution (Seventy-first Amendment) Act, 1992, s. 2 (w.e.f. 31-8-1992).5. Entry 8 renumbered as entry 11 by the Constitution (Ninety-second Amendment) Act, 2003, s. 2 (w.e.f. 7-1-2004).6. Entries 9 to 14 renumbered as entries 12 to 17 by s. 2,ibid.(w.e.f. 7-1-2004).7. Subs. by the Constitution (Ninety-sixth Amendment) Act, 2011, s. 2, for "Oriya" (w.e.f. 23-9-2011).'''), 
# 	Document(
# 		metadata={
# 			'producer': 'iLovePDF', 
# 			'creator': 'PyPDF', 
# 			'creationdate': '', 
# 			'moddate': '2024-07-01T11:20:33+00:00', 
# 			'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
# 			'total_pages': 402, 
# 			'page': 356, 
# 			'page_label': '357'
# 		}, 
# 	page_content='''THE CONSTITUTION OF  INDIA(Eighth Schedule)3261[18.  Santhali.]2[3[19.] Sindhi.]4[20.] Tamil.4[21.] Telugu.           4[22.]  Urdu.   ______________________________________________1. Ins. by the Constitution (Ninety-second Amendment) Act, 2003, s. 2 (w.e.f. 7-1-2004).2. Added by the Constitution (Twenty-first Amendment) Act, 1967, s. 2 (w.e.f. 10-4-1967).  3. Entry 15 renumbered as entry 19 by the Constitution (Ninety-second Amendment) Act, 2003, s. 2 (w.e.f. 7-1-2004).4. Entries 16 to 18 renumbered as entries 20 to 22 by s. 2, ibid. (w.e.f. 7-1-2004).'''), 
# 	Document(
# 		metadata={
# 			'producer': 'iLovePDF', 
# 			'creator': 'PyPDF', 
# 			'creationdate': '', 
# 			'moddate': '2024-07-01T11:20:33+00:00', 
# 			'source': 'D:\\Python Projects\\llm_training\\7. document_loaders\\data\\constitution of India.pdf', 
# 			'total_pages': 402, 
# 			'page': 357, 
# 			'page_label': '358'
# 		}, 
# 		page_content='''327
# 1[NINTH SCHEDULE(Article 31B)1. The Bihar Land Reforms Act, 1950 (Bihar Act XXX of 1950).2. The Bombay Tenancy and Agricultural Lands Act, 1948. (Bombay Act LXVII of 1948). 3. The Bombay Maleki Tenure Abolition Act, 1949 (Bombay Act LXI of 1949).4. The Bombay Taluqdari Tenure Abolition Act, 1949. (Bombay Act LXII of 1949). 5. The Panch Mahals Mehwassi Tenure Abolition Act, 1949. (Bombay Act LXIII of 1949).6. The Bombay Khoti Abolition Act, 1950 (Bombay Act VI of 1950).7. The Bombay Paragana and Kulkarni Watan Abolition Act, 1950. (Bombay Act LX of 1950).8. The Madhya Pradesh Abolition of Proprietary Rights (Estates, Mahals, Alienated Lands) Act, 1950 (Madhya Pradesh Act I of 1951).9. The Madras Estates (Abolition and Conversion into Ryotwari) Act, 1948 (Madras Act XXVI of 1948). 10. The Madras Estates (Abolition and Conversion into Ryotwari) Amendment Act, 1950 (Madras Act I of 1950).11. The Uttar Pradesh  Zamindari Abolition and Land Reforms Act, 1950 (Uttar Pradesh Act I of 1951).12. The Hyderabad (Abolition of Jagirs) Regulation, 1358F (No. LXIX of 1358, Fasli).13. The Hyderabad Jagirs (Commutation) Regulation, 1359F (No. XXV of 1359, Fasli).]2[14. The Bihar Displaced Persons Rehabilitation (Acquisition of Land) Act, 1950 (Bihar Act XXXVIII of 1950). 15. The United Provinces Land Acquisition (Rehabilitation of Refugees) Act, 1948 (U.P. Act XXVI of 1948).16. The Resettlement of Displaced Persons (Land Acquisition) Act, 1948 (Act LX of 1948).17. Sections 52A to 52G of the Insurance Act, 1938 (Act IV of 1938), as inserted by section 42 of the Insurance (Amendment) Act, 1950 (Act XLVII of 1950).18. The Railway Companies (Emergency Provisions) Act, 1951 (Act LI of 1951).______________________________________________1. Ninth Schedule (entries 1 to 13) added by the Constitution (First Amendment)Act, 1951, s. 14 (w.e.f. 18-6-1951).2. Ninth Schedule (entries 14 to 20) added by the Constitution (Fourth Amendment) Act, 1955, s. 5 (w.e.f. 27-4-1955).'''
# 	)
# ]
[Finished in 75.8s]