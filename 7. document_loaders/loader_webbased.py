from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import BaseModel, Field
from typing import List

from dotenv import load_dotenv

load_dotenv()

class QAFormat(BaseModel):
    question: str = Field(description="The question being asked")
    answer: str = Field(description="The answer to the question")

class QAList(BaseModel):
    qa_pairs: List[QAFormat] = Field(description="List of question-answer pairs")

JSONparser = JsonOutputParser(pydantic_object=QAList)
parser = StrOutputParser()

model = ChatOpenAI()

prompt = PromptTemplate(
	template="""
	Answer the following question using given product info. Product info could be messy, so, extract answers into format
	{format_instructions}

	text: {text}
	queries: {query}
	""",
	input_variables=['text', 'query'],
	partial_variables={"format_instructions": JSONparser.get_format_instructions()},
)

url = "https://www.flipkart.com/samsung-183-l-direct-cool-single-door-4-star-refrigerator-base-drawer-digital-inverter/p/itm0e72f8c5beb0d?pid=RFRGHJPXATRDHYHF&lid=LSTRFRGHJPXATRDHYHFHFTCA4&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_c07de317-9693-445e-9250-46d384ff80bf_16_1TRW7YRA9FKG_MC.RFRGHJPXATRDHYHF&ppt=hp&ppn=homepage&ssid=c9xfa1hdeo0000001748500357296&otracker=clp_pmu_v2_Single-door%2BRefrigerators_1_16.productCard.PMU_V2_SAMSUNG%2B183%2BL%2BDirect%2BCool%2BSingle%2BDoor%2B4%2BStar%2BRefrigerator%2Bwith%2BBase%2BDrawer%2B%2Bwith%2BDigital%2BInverter_tvs-and-appliances-new-clp-store_RFRGHJPXATRDHYHF_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Single-door%2BRefrigerators_LIST_productCard_cc_1_NA_view-all&cid=RFRGHJPXATRDHYHF"
loader = WebBaseLoader(web_path=url)
documents = loader.load()

chain = prompt | model | parser

result = chain.invoke(dict(query="""
	1. Give me basic features of Product.
	2. What is price of product. and is there any other product with which we can compare our price.
	3. What are reviewers say, is it a good product or not.
	""",
	text=documents[0].page_content))

print(result)

# {
#     "qa_pairs": [
#         {
#             "question": "Give me basic features of Product.",
#             "answer": "Capacity: 183 L, Star Rating: 4, Defrosting Type: Direct Cool, Compressor Type: Digital Inverter Compressor, Built-in Stabilizer: Yes, Toughened Glass Shelves: Yes"
#         },
#         {
#             "question": "What is price of product. and is there any other product with which we can compare our price.",
#             "answer": "Price of the product is ₹16,390 with 28% off from original price of ₹22,999. Another related product is V-Guard VG 50 Supreme (Grey) Stabilizer for Refrigerators available at ₹1,879."
#         },
#         {
#             "question": "What are reviewers say, is it a good product or not.",
#             "answer": "Reviewers generally rate the product positively, with an average rating of 4.5 stars based on 81,423 ratings and 5,196 reviews. Positive comments include it being value for money, good for small families, nice design, and good performance."
#         }
#     ]
# }

# print(documents)





# [Document(
# 	metadata={
# 		'source': 
# 			'https://www.flipkart.com/samsung-183-l-direct-cool-single-door-4-star-refrigerator-base-drawer-digital-inverter/p/itm0e72f8c5beb0d?pid=RFRGHJPXATRDHYHF&lid=LSTRFRGHJPXATRDHYHFHFTCA4&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_c07de317-9693-445e-9250-46d384ff80bf_16_1TRW7YRA9FKG_MC.RFRGHJPXATRDHYHF&ppt=hp&ppn=homepage&ssid=c9xfa1hdeo0000001748500357296&otracker=clp_pmu_v2_Single-door%2BRefrigerators_1_16.productCard.PMU_V2_SAMSUNG%2B183%2BL%2BDirect%2BCool%2BSingle%2BDoor%2B4%2BStar%2BRefrigerator%2Bwith%2BBase%2BDrawer%2B%2Bwith%2BDigital%2BInverter_tvs-and-appliances-new-clp-store_RFRGHJPXATRDHYHF_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Single-door%2BRefrigerators_LIST_productCard_cc_1_NA_view-all&cid=RFRGHJPXATRDHYHF', 
# 		'title': 
# 			'SAMSUNG 183 L Direct Cool Single Door 4 Star Refrigerator with Base Drawer  with Digital Inverter Online at Best Price in India | Flipkart.com', 
# 		'language': 'en'
# 	}, 
# 	page_content="""SAMSUNG 183 L Direct Cool Single Door 4 Star Refrigerator with Base Drawer  with Digital Inverter Online at Best Price in India | Flipkart.com        Explore PlusLoginBecome a Seller More CartAdd to cart Buy NowHomeHome & KitchenHome AppliancesRefrigeratorsSAMSUNG RefrigeratorsSAMSUNG 183 L Direct Cool Single Door 4 Star Refrigerator with Base Drawer  with Digital Inverter (Camellia Blue, RR20C1824CU/HL)
# 	CompareShareSAMSUNG 183 L Direct Cool Single Door 4 Star Refrigerator with Base Drawer  with Digital Inverter\xa0\xa0(Camellia Blue, RR20C1824CU/HL)4.581,423 Ratings\xa0&\xa05,196 Reviews₹16,390₹22,99928% offi+ ₹79 Protect Promise Fee\xa0Learn moreSecure delivery by 1 Jun, SundayAvailable offersBank Offer5% Unlimited Cashback on Flipkart Axis Bank Credit CardT&CBank OfferGet additional ₹250 off on Debit, Credit cards and UPI TransactionsT&CBank OfferGet additional ₹750 off on Debit, Credit cards and UPI TransactionsT&CNo Cost EMI on Bajaj Finserv Credit CardsT&CView 2 more offersBuy without Exchange₹16,390Buy with Exchangeup to ₹8,500 offEnter pincode to check if exchange is available1 year comprehensive warranty on the product, 20 years on compressor by the brand.Know MoreWith Base DrawerYesYesPlease select a With Base Drawer to proceed✕ColorCamellia BlueCamellia PurpleHimalaya Poppy Blue3 morePlease select a Color to proceed✕Star Rating4455Please select a Star Rating to proceed✕DeliveryCheckEnter pincodeDelivery by1 Jun, Sunday|Free₹40?if ordered before 2:06 PMView Details Learn more about Flipkart delivery and installation process Watch VideoHighlights183 L : Good for couples and small familiesDigital Inverter Compressor4 Star : For Energy savings up to 45%Direct Cool : Economical, consumes less electricity, requires manual defrostingBase Stand with Drawer : For storing items that don't need cooling (Onion, Potato etc.)Easy Payment OptionsCash on DeliveryNet banking & Credit/ Debit/ ATM cardView DetailsImportant NoteThis item does not require installation and can be self-installed easily.SellerAkshnav Online4.47 Days Service Center Replacement/Repair?GST invoice available?See other sellersDescriptionHigh-performance and practical, the Samsung Refrigerator is an exceptional addition to your kitchen. It offers energy efficiency, minimal operating noise, and long-lasting durability with its Digital Inverter technology. And, the Digital Inverter Compressor in this refrigerator automatically changes its speed in response to cooling needs. Also, this refrigerator is protected from voltage fluctuations because it operates with a wide voltage range of 100 V to up to 300 V. Moreover, without requiring a stabiliser, it can keep running steadily and smoothly.Read MoreProduct DescriptionDigital Inverter Technology (DIT)Thanks to its Digital Inverter technology, the Samsung Refrigerator facilitates energy efficiency, low operational noise, and long-lasting durability. Additionally, in response to the cooling requirements, this refrigerator's Digital Inverter Compressor automatically modifies its speed.
# 	Stabiliser-free OperationAs this refrigerator functions with a wide voltage range of 100 V to up to 300 V, it is protected from voltage fluctuations. In addition, its stabiliser-free operation enables it to continue operating smoothly and stably. Besides, if there's a significant increase in the voltage, the power is immediately cut off to prevent electrical damage.
# 	Base Stand with DrawerYou can keep your vegetables at room temperature in this refrigerator. Its lower section has a sizable base stand drawer that is a practical spot to keep all of your food items, including onions and potatoes, that do not need cooling. This way, you won't have to lose kitchen space or use additional storage baskets.
# 	Additional Bottle SpaceWithout taking up additional space, this refrigerator's Deep Door Guard can securely store big bottles, large milk and juice cartons, and other beverages. Besides, you can keep up to three 2 L bottles along with a 1 L bottle inside the door at once.
# 	Fresh RoomFeaturing a Fresh Room, this refrigerator has a significantly cool section that offers freshness even if the door is opened frequently. So, you can store your green salad and dairy products, including cheese, in this place to keep them fresh for a long period of time.
# 	Operates on Home Inverter+This Smart Connect Inverter technology-enabled refrigerator can continue to operate even when there is a power outage, ensuring that your food is always fresh.
# 	Runs with Solar EnergyAs it produces electricity with a voltage range of 100 V to 300 V using a solar panel, this refrigerator can help with environmental protection. And, its solar charge controller regulates the voltage and current in the batteries. Moreover, the SPCU draws electricity from the batteries' stored energy in the evening to run this refrigerator.
# 	Safe Clean BackOwing to its Safe Clean Back, this refrigerator features a smooth safety cover that safeguards its internal essential parts and can conveniently be wiped clean. It protects them from accidental bumps and knocks as well as extends their lifespan and gives them a clean appearance.
# 	Antibacterial GasketSporting an antibacterial gasket, this refrigerator ensures that its door liner stays clean, while also preventing fungus and bacteria from building up inside. This keeps everything in the refrigerator clean and prevents food from spoiling rapidly.
# 	Freezer RoomWith a freezer room, this refrigerator provides rapid cooling to keep your food fresh, and drinks cold and offers large quantities of ice. With the simple touch of a button, this refrigerator's Power Cool rapidly cools down food stored on the fridge shelves while Power Freeze quickly makes ice.
# 	Bright LampEquipped with a safe and energy-efficient bright lamp inside, this refrigerator ensures that finding your food and fresh items is a breeze.
# 	Sturdy ShelvesConstructed with toughened glass, this refrigerator's shelves can effortlessly and securely support loads weighing up to 175 kg. This allows you to easily store even heavy food containers and utensils.
# 	View all featuresSpecificationsImportant NoteAs a part of the "Energy Labelling Plan" of the Bureau of Energy Efficiency, the star rating of Refrigerators effective 1st January 2023 onwards will be one star less than its rating from 1st Jan 2020 to 31st December 2022.GeneralIn The Box1 Refrigerator Unit, User Manual, Warranty CardTypeSingle DoorRefrigerator TypeTop MountDefrosting TypeDirect CoolCompressor TypeDigital Inverter CompressorCapacity183 LNumber of Doors1Star Rating4Toughened GlassYesBuilt-in StabilizerYesPerformance FeaturesTemperature ControlYesConvertible RefrigeratorNoBody And Design FeaturesShelf MaterialToughened GlassConvenience FeaturesDeodorizerYesFlexible RackYesPower FeaturesPower RequirementAC 220 - 240 V, 50 HzBEE Rating Year2024Stabilizer RequiredNoRefrigerator Comparment FeaturesRefrigerator Interior LightYesEgg TrayYesFreezer Compartment FeaturesIce Cube Tray TypeTray Ice MakerAdditional FeaturesLaunch Year2024DimensionsNet Height130 cmNet Depth64 cmNet Width54.9 mmWeight39 kgInstallation & DemoInstallation & DemoThis product does not require installation. The features of the product are presented in the user manual that comes with it. Hence, the manufacturer does not provide on-site installation or demo for the product. In case of any queries about the installation or the features of product, kindly call us at 1800 208 9898 or (080) 49400000 for assistance.WarrantyWarranty Service TypeFor any warranty related issues, please call the Customer Support - [1800 40 7267864][https://www.samsung.com/in/microsite/samsung-mall/contact-us/]Warranty Summary1 year comprehensive warranty on the product, 20 years on compressor by the brand.Covered in WarrantyAll Parts Excluding Plastic Parts, Glassware, Bulb and Tube from the Date of Purchase Against Defective Material and WorkmanshipNot Covered in WarrantyParts: Plastic, Glassware, Bulb, Tube. Any Accessories External to the Product. The Product is Not Used According to the Instructions Given in the Instructions Manual. Defects Caused by Improper Use as Determined by the Company Personnel. Modification or Alteration of Any Nature made in the Electrical Circuitry or Physical Construction of the Set. Site (Where the Premises is Kept) Conditions That do Not Confirm to the Recommended Operating Conditions of the Machine. The Serial Number is Removed, Altered or Obliterated from the Machine. Defects Due to Cause Beyond Control Like Lightening, Abnormal Voltage, Acts of God or While in Transit to the Service Centres or Purchasers ResidenceRead MoreFrequently Bought TogetherSAMSUNG 183 L Direct Cool Single Door 4 Star Refrigerator with Ba...4.5(81,423)₹16,390₹22,99928% offV-Guard VG 50 Supreme (Grey) Stabilizer for Refrigerators up to 3...4.1(3,151)₹1,8791 Item₹16,3901 Add-on₹1,879Total₹18,269Add 2 Items to CartRatings & ReviewsRate Product4.5★81,423 Ratings &5,196 Reviews5★4★3★2★1★53,74419,1034,2711,3102,9954.4Performance4.4Design & Features4.3Value for Money4.2Delivery & Installation+ 19715Super!Nice product... value for money For small family that's okGo for it guy's 😉READ MOREshivendra prajapatiCertified Buyer, AllahabadDec, 2023951253PermalinkReport Abuse5WonderfulFabulousREAD MOREDeepesh  JiiiCertified Buyer, Samastipur DistrictMay, 202420053PermalinkReport Abuse5Great productNice product.It's been 16 days since I bought it 16 days I'm posting a comment so far I don't see any kind of problem or if there is any problem I will commentREAD MORERajesh PCertified Buyer, GandhigramMay, 20248120PermalinkReport Abuse5BrilliantGood product 👌READ MORENandwana Damji  Babubhai Certified Buyer, JamnagarMar, 20245914PermalinkReport Abuse5Worst experience ever!In two days no cooling happeningREAD MOREHarshvardhansinh JadejaCertified Buyer, SambraMar, 2024223PermalinkReport Abuse4Good choiceMy mom is very happyREAD MOREMoinur Moinur hasanCertified Buyer, North Twenty Four Parganas DistrictMay, 202320768PermalinkReport Abuse5Mind-blowing purchaseVery good productThank you Flipkart ❤️❤️💕And very valuable 🙏🙏READ MOREBit tuCertified Buyer, KolkataMar, 2024193PermalinkReport Abuse5Worth every pennyExcellentREAD MORERohit BhartiCertified Buyer, BegusaraiJul, 20236319PermalinkReport Abuse5Fabulous!Looking very beautifull  but instalation late but product good best quality Samsung'sREAD MOREKallipilli santosh  Kumar Certified Buyer, ParlakhemundiJun, 20236923PermalinkReport Abuse5Must buy!Wow super fridge very nice product thank you for Flipkart delivery also fast price also nice thank you so much FlipkartREAD MOREShahida AktarCertified Buyer, Penha De FrancaMay, 20234714PermalinkReport Abuse+All 5196 reviewsQuestions and AnswersQ:Is there any heating issue more than normal ......????A:2 side heating problem hai. Kya sabhi refrigerators me ye normal rehti haiAnonymousCertified Buyer2811Report AbuseRead other answersQ:How is the backside?A:Metal body in the backside with water outlet box .Azharuddin  Mansuri Certified Buyer7526Report AbuseQ:How many watt requiredA:The 4 star rated one is actually just 50 watts. It's written inside the refrigerator on a sticker.Samrat RajCertified Buyer4927Report AbuseRead other answersQ:Is it metal or steel outer covering or plasticA:PlasticNishat ParveenCertified Buyer3423Report AbuseRead other answersQ:Stabilizer requires to refrigerateA:NoAnonymousCertified Buyer61Report AbuseQ:Which year model ????A:2024AnonymousCertified Buyer94Report AbuseQ:Door lock available?A:YesAnonymousCertified Buyer51Report AbuseRead other answersQ:Running time out side Body Is too Hot any Problem in this ProductA:Yes on Running time outer body is too hot.SURENDRA  KUMARCertified Buyer41Report AbuseQ:How much electric bill in one dayA:For power consumption it is good, but it some time over heatingVENKY HARKAVATHCertified Buyer73Report AbuseQ:How many month guaranteeA:12 MonthsAnonymousCertified Buyer20Report AbuseAll questions+Safe and Secure Payments.Easy returns.100% Authentic products.You might be interested inBedsMin. 50% OffShop NowFansMin. 50% OffShop NowVoltage StabilizersMin. 50% OffShop NowWashing MachinesMin. 50% OffShop NowTop Stories:Brand DirectoryMOST SEARCHED IN Home & Kitchen:BLACK & DECKERCAMERA TRIPODCANON EOS 700DFM RADIO WITH USBSLIMMING BELTPHILIPS STRAIGHTENER PRICEREMINGTON HAIR STRAIGHTENERLG INDIA TVSAMSUNG LEDLED SONYCOOLER WITHOUT WATERBAJAJ HOME APPLIANCESTOWER FANSWASHING MACHINE VIDEOCONWATER FILTER ONLINEHAND BLENDER ONLINEINDUCTION COOKTOPINTEX LED TVD5100PHILIPS QT4011 15SAMSUNG DOUBLE DOOR REFRIGERATORBLUE STAR 1.5 TON SPLIT ACBLUE STAR 1.5 TON ACCARRIER WINDOW ACHAIER AC 1 TONO GENERAL WINDOW ACSAMSUNG INVERTER AC 1.5 TONIFB WASHING MACHINE COVERSONY 32 INCH FULL HD SMART TVWATER FILTERABOUTContact UsAbout UsCareersFlipkart StoriesPressCorporate InformationGROUP COMPANIESMyntraCleartripShopsyHELPPaymentsShippingCancellation & ReturnsFAQCONSUMER POLICYCancellation & ReturnsTerms Of UseSecurityPrivacySitemapGrievance RedressalEPR ComplianceMail Us:Flipkart Internet Private Limited, 
# 	 Buildings Alyssa, Begonia & 
# 	 Clove Embassy Tech Village, 
# 	 Outer Ring Road, Devarabeesanahalli Village, 
# 	 Bengaluru, 560103, 
# 	 Karnataka, India
# 	 SocialRegistered Office Address:Flipkart Internet Private Limited, 
# 	 Buildings Alyssa, Begonia & 
# 	 Clove Embassy Tech Village, 
# 	 Outer Ring Road, Devarabeesanahalli Village, 
# 	 Bengaluru, 560103, 
# 	 Karnataka, India 
# 	 CIN : U51109KA2012PTC066107 
# 	 Telephone: 044-45614700 / 044-67415800
# 	 Become a SellerAdvertiseGift CardsHelp Center© 2007-2025 Flipkart.comBack to top   

# """)]