import streamlit as st


LANGUAGES = {
    "English": "en",
    "हिंदी": "hi",
    "தமிழ்": "ta",
    "తెలుగు": "te",
    "ಕನ್ನಡ": "kn",
    "മലയാളം": "ml",
    "বাংলা": "bn",
    "मराठी": "mr",
}

STATE_LANGUAGES = {
    "Tamil Nadu": "தமிழ்",
    "Andhra Pradesh": "తెలుగు",
    "Telangana": "తెలుగు",
    "Karnataka": "ಕನ್ನಡ",
    "Kerala": "മലയാളം",
    "West Bengal": "বাংলা",
    "Maharashtra": "मराठी",
    "Delhi": "हिंदी",
}

TEXT = {
    "en": {
        "home":"Home","explore":"Explore Schemes","how":"How It Works","about":"About",
        "find":"Find My Schemes","find_cta":"Find Schemes for Me",
        "hero_title":"Discover government schemes made for you",
        "hero_subtitle":"Find benefits, scholarships and financial help based on your needs.",
        "trust":"Information from official government portals",
        "opportunities":"EXPLORE OPPORTUNITIES",
        "op_title":"Government support for every stage of life",
        "op_subtitle":"Choose a category to see related schemes.",
        "how_title":"Three simple steps","how_subtitle":"From your details to a clearer application path.",
        "step1":"Share your details","step1_desc":"Tell us your age, state, income and category.",
        "step2":"Check matching schemes","step2_desc":"We compare your details with official scheme rules.",
        "step3":"Prepare and apply","step3_desc":"Review documents and apply only on the official website.",
        "cta_title":"Every Citizen. Every Opportunity.","cta_subtitle":"Discover. Understand. Apply.",
        "voice_hint":"Large text, clear icons and simple language",
        "recommendation_profile_warning":"Complete your profile to see personalized recommendations.",
        "go_profile":"Go to Profile","assessment":"YOUR INITIAL ASSESSMENT","recommended_title":"Recommended Schemes",
        "assessment_hint":"These statuses are initial rule-based assessments, not approval or eligibility guarantees.",
        "explorer":"SCHEME EXPLORER","explorer_title":"Browse Government Schemes","shortlist":"YOUR SHORTLIST","saved_title":"Saved Schemes",
    },
    "hi": {
        "home":"मुखपृष्ठ","explore":"योजनाएं देखें","how":"कैसे काम करता है","about":"परिचय",
        "find":"मेरी योजनाएं खोजें","find_cta":"मेरे लिए योजनाएं खोजें",
        "hero_title":"आपके लिए सरकारी योजनाएं खोजें",
        "hero_subtitle":"अपनी जरूरत के अनुसार लाभ, छात्रवृत्ति और वित्तीय सहायता खोजें.",
        "trust":"आधिकारिक सरकारी पोर्टलों से जानकारी",
        "opportunities":"अवसर देखें","op_title":"जीवन के हर चरण के लिए सरकारी सहायता",
        "op_subtitle":"संबंधित योजनाएं देखने के लिए एक श्रेणी चुनें.",
        "how_title":"तीन आसान चरण","how_subtitle":"अपनी जानकारी से स्पष्ट आवेदन प्रक्रिया तक.",
        "step1":"अपनी जानकारी दें","step1_desc":"अपनी आयु, राज्य, आय और श्रेणी बताएं.",
        "step2":"मिलती योजनाएं देखें","step2_desc":"हम आपकी जानकारी को सरकारी नियमों से मिलाते हैं.",
        "step3":"तैयार करें और आवेदन करें","step3_desc":"कागजात देखें और केवल आधिकारिक वेबसाइट पर आवेदन करें.",
        "cta_title":"हर नागरिक. हर अवसर.","cta_subtitle":"खोजें. समझें. आवेदन करें.",
        "voice_hint":"बड़ा टेक्स्ट, स्पष्ट आइकन और सरल भाषा",
        "recommendation_profile_warning":"व्यक्तिगत योजनाएं देखने के लिए अपनी जानकारी पूरी करें.",
        "go_profile":"जानकारी भरें","assessment":"प्रारंभिक मूल्यांकन","recommended_title":"अनुशंसित योजनाएं",
        "assessment_hint":"यह प्रारंभिक नियम-आधारित मूल्यांकन है, सरकारी स्वीकृति नहीं.",
        "explorer":"योजना खोज","explorer_title":"सरकारी योजनाएं देखें","shortlist":"आपकी पसंद","saved_title":"सहेजी गई योजनाएं",
    },
    "ta": {
        "home":"முகப்பு","explore":"திட்டங்களை காண்க","how":"எப்படி செயல்படும்","about":"எம்மைப் பற்றி",
        "find":"எனக்கு திட்டங்கள்","find_cta":"எனக்கான திட்டங்களை காண்க",
        "hero_title":"உங்களுக்கான அரசு திட்டங்களைக் கண்டறியுங்கள்",
        "hero_subtitle":"உங்கள் தேவை அடிப்படையில் பலன்கள், உதவித்தொகை, நிதி உதவி கண்டறியுங்கள்.",
        "trust":"அதிகாரப்பூர்வ அரசு இணையதளங்களிலிருந்து தகவல்",
        "opportunities":"வாய்ப்புகளை காண்க","op_title":"வாழ்க்கையின் ஒவ்வொரு கட்டத்திற்கும் அரசு ஆதரவு",
        "op_subtitle":"தொடர்புடைய திட்டங்களை காண வகையை தேர்வு செய்யவும்.",
        "how_title":"மூன்று எளிய படிகள்","how_subtitle":"உங்கள் விவரத்திலிருந்து விண்ணப்ப வழி வரை.",
        "step1":"உங்கள் விவரத்தை பகிரவும்","step1_desc":"வயது, மாநிலம், வருமானம் மற்றும் வகையை சொல்லுங்கள்.",
        "step2":"பொருந்தும் திட்டங்களை காண்க","step2_desc":"உங்கள் விவரங்களை அரசு விதிகளுடன் ஒப்பிடுவோம்.",
        "step3":"தயார் செய்து விண்ணப்பிக்கவும்","step3_desc":"ஆவணங்களை சரிபார்த்து அதிகாரப்பூர்வ தளத்தில் மட்டுமே விண்ணப்பிக்கவும்.",
        "cta_title":"ஒவ்வொரு குடிமகனும். ஒவ்வொரு வாய்ப்பும்.","cta_subtitle":"கண்டறி. புரிந்து கொள். விண்ணப்பி.",
        "voice_hint":"பெரிய எழுத்து, தெளிவான படங்கள் மற்றும் எளிய மொழி",
        "recommendation_profile_warning":"தனிப்பட்ட பரிந்துரைகளை பார்க்க உங்கள் விவரத்தை முடிக்கவும்.",
        "go_profile":"சுயவிவரம்","assessment":"ஆரம்ப மதிப்பீடு","recommended_title":"பரிந்துரைக்கப்பட்ட திட்டங்கள்",
        "assessment_hint":"இது ஆரம்ப விதி அடிப்படையிலான மதிப்பீடு மட்டுமே, அரசு ஒப்புதல் அல்ல.",
        "explorer":"திட்டங்கள்","explorer_title":"அரசுத் திட்டங்களைப் பாருங்கள்","shortlist":"சேமித்தவை","saved_title":"சேமித்த திட்டங்கள்",
    },
    "te": {
        "home":"హోమ్","explore":"పథకాలు చూడండి","how":"ఎలా పని చేస్తుంది","about":"గురించి",
        "find":"నాకు పథకాలు","find_cta":"నాకు పథకాలు కనుగొనండి",
        "hero_title":"మీకు చెందిన ప్రభుత్వ పథకాలను కనుగొనండి",
        "hero_subtitle":"మీ అవసరాలకు సరిపోయే ప్రయోజనాలు, స్కాలర్షిప్‌లు మరియు సహాయం చూడండి.",
        "trust":"అధికారిక ప్రభుత్వ పోర్టళ్ల సమాచారం","opportunities":"అవసరాలను చూడండి",
        "op_title":"ప్రతి జీవిత దశకు ప్రభుత్వ సహాయం","op_subtitle":"సంబంధిత పథకాలు చూడటానికి వర్గం ఎంచుకోండి.",
        "how_title":"మూడు సరళమైన అంచెలు","how_subtitle":"మీ వివరాల నుండి దరఖాస్తు మార్గం వరకు.",
        "step1":"మీ వివరాలు చెప్పండి","step1_desc":"వయసు, రాష్ట్రం, ఆదాయం మరియు వర్గం చెప్పండి.",
        "step2":"సరిపోలే పథకాలు చూడండి","step2_desc":"మీ వివరాలను అధికారిక పథక నిబంధనలతో పోలుస్తాము.",
        "step3":"తయారు చేసి దరఖాస్తు చేయండి","step3_desc":"పత్రాలు చూసి అధికారిక వెబ్సైట్‌లో మాత్రమే దరఖాస్తు చేయండి.",
        "cta_title":"ప్రతి పౌరుడు. ప్రతి అవకాశం.","cta_subtitle":"కనుగొను. అర్థం చేసుకో. దరఖాస్తు చేయి.",
        "voice_hint":"పెద్ద అక్షరాలు, స్పష్టమైన చిహ్నాలు",
        "recommendation_profile_warning":"పథకాలను చూడటానికి వివరాలు పూర్తి చేయండి.","go_profile":"ప్రొఫైల్","assessment":"ప్రాథమిక అంచనా","recommended_title":"సిఫారసు పథకాలు","assessment_hint":"ఇది ప్రాథమిక అంచనా మాత్రమే.","explorer":"పథకాలు","explorer_title":"ప్రభుత్వ పథకాలు","shortlist":"సేవ్ చేసినవి","saved_title":"సేవ్ చేసిన పథకాలు",
    },
    "kn": {
        "home":"ಮುಖ್ಯಪುಟ","explore":"ಯೋಜನೆಗಳನ್ನು ನೋಡಿ","how":"ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ","about":"ಬಗ್ಗೆ",
        "find":"ನನಗೆ ಯೋಜನೆಗಳು","find_cta":"ನನಗೆ ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ",
        "hero_title":"ನಿಮಗೆ ಸಂಬಂಧಿಸಿದ सरकारी ಯೋಜನೆಗಳನ್ನು ಕಂಡುಕೊಳ್ಳಿ",
        "hero_subtitle":"ನಿಮ್ಮ ಅಗತ್ಯಕ್ಕೆ ಅನುಗುಣವಾದ ಪ್ರಯೋಜನಗಳು ಮತ್ತು ಸಹಾಯವನ್ನು ನೋಡಿ.",
        "trust":"ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್ ಮಾಹಿತಿ","opportunities":"ಅವಕಾಶಗಳನ್ನು ನೋಡಿ",
        "op_title":"ಜೀವನದ ಪ್ರತಿ ಹಂತಕ್ಕೆ ಸರ್ಕಾರಿ ಬೆಂಬಲ","op_subtitle":"ಸಂಬಂಧಿತ ಯೋಜನೆಗಳಿಗಾಗಿ ವರ್ಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "how_title":"ಮೂರು ಸರಳ ಹಂತಗಳು","how_subtitle":"ನಿಮ್ಮ ವಿವರಗಳಿಂದ ಅರ್ಜಿ ಮಾರ್ಗದರ್ಶಿ.",
        "step1":"ನಿಮ್ಮ ವಿವರಗಳನ್ನು ನೀಡಿ","step1_desc":"ವಯಸ್ಸು, ರಾಜ್ಯ, ಆದಾಯ ಮತ್ತು ವರ್ಗ ತಿಳಿಸಿ.",
        "step2":"ಹೊಂದುವ ಯೋಜನೆಗಳನ್ನು ನೋಡಿ","step2_desc":"ನಿಮ್ಮ ವಿವರಗಳನ್ನು ಅಧಿಕೃತ ನಿಯಮಗಳೊಂದಿಗೆ ಹೋಲಿಸುತ್ತೇವೆ.",
        "step3":"ಸಿದ್ಧಪಡಿಸಿ ಮತ್ತು ಅರ್ಜಿ ಸಲ್ಲಿಸಿ","step3_desc":"ದಾಖಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಅಧಿಕೃತ ಸೈಟ್ನಲ್ಲಿ ಮಾತ್ರ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
        "cta_title":"ಪ್ರತಿ ನಾಗರಿಕ. ಪ್ರತಿ ಅವಕಾಶ.","cta_subtitle":"ಕಂಡುಹಿಡಿ. ಅರ್ಥಮಾಡಿ. ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
        "voice_hint":"ದೊಡ್ಡ ಅಕ್ಷರ ಮತ್ತು ಸರಳ ಭಾಷೆ",
        "recommendation_profile_warning":"ಪರಿಣಾಮಗಳನ್ನು ನೋಡಲು ವಿವರಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ.","go_profile":"ಪ್ರೊಫೈಲ್","assessment":"ಪ್ರಾಥಮಿಕ ಮೌಲ್ಯಮಾಪನ","recommended_title":"ಶಿಫಾರಸು ಯೋಜನೆಗಳು","assessment_hint":"ಇದು ಪ್ರಾಥಮಿಕ ನಿಯಮ ಆಧಾರಿತ ಮೌಲ್ಯಮಾಪನ.","explorer":"ಯೋಜನೆಗಳು","explorer_title":"ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು","shortlist":"ಉಳಿಸಿದವು","saved_title":"ಉಳಿಸಿದ ಯೋಜನೆಗಳು",
    },
    "ml": {
        "home":"ഹോം","explore":"പദ്ധതികൾ കാണുക","how":"എങ്ങനെ പ്രവർത്തിക്കും","about":"വിവരണം",
        "find":"എന്റെ പദ്ധതികൾ","find_cta":"എനിക്കായി പദ്ധതികൾ കണ്ടെത്തുക",
        "hero_title":"നിങ്ങൾക്ക് ഉചിതമായ സർക്കാർ പദ്ധതികൾ കണ്ടെത്തുക",
        "hero_subtitle":"നിങ്ങളുടെ ആവശ്യത്തിന് അനുയോജ്യമായ സഹായങ്ങളും പ്രോത്സാഹനങ്ങളും കണ്ടെത്തുക.",
        "trust":"ഔദ്യോഗിക സർക്കാർ പോർട്ടലുകൾ","opportunities":"സാധ്യതകൾ കാണുക",
        "op_title":"ജീവിതത്തിന്റെ എല്ലാ ഘട്ടങ്ങളിലും സർക്കാർ സഹായം","op_subtitle":"ബന്ധപ്പെട്ട പദ്ധതികൾക്കായി വിഭാഗം തിരഞ്ഞെടുക്കുക.",
        "how_title":"മൂന്ന് ലളിതമായ ഘട്ടങ്ങൾ","how_subtitle":"വിവരങ്ങളിൽ നിന്ന് അപേക്ഷാ വഴിവരെ.",
        "step1":"വിവരങ്ങൾ പങ്കിടുക","step1_desc":"വയസ്സും സംസ്ഥാനും വരുമാനവും വിഭാഗവും നൽകുക.",
        "step2":"പൊരുത്തമുള്ള പദ്ധതികൾ","step2_desc":"നിങ്ങളുടെ വിവരങ്ങൾ ഔദ്യോഗിക നിബന്ധനകളോടു താരതമ്യം ചെയ്യും.",
        "step3":"തയ്യാറാക്കി അപേക്ഷിക്കുക","step3_desc":"രേഖകൾ പരിശോധിച്ച് ഔദ്യോഗിക സൈറ്റിൽ മാത്രം അപേക്ഷിക്കുക.",
        "cta_title":"ഓരോ പൗരനും. ഓരോ അവസരവും.","cta_subtitle":"കണ്ടെത്തുക. മനസ്സിലാക്കുക. അപേക്ഷിക്കുക.",
        "voice_hint":"വലിയ അക്ഷരം, स्पष्ट pictograms",
        "recommendation_profile_warning":"പരാമർശങ്ങൾ കാണാൻ വിവരങ്ങൾ പൂർത്തിയാക്കുക.","go_profile":"പ്രൊഫൈൽ","assessment":"പ്രാഥമിക വിലയിരുത്തൽ","recommended_title":"ശുപാർശ ചെയ്യുന്ന പദ്ധതികൾ","assessment_hint":"ഇത് പ്രാഥമിക നിയമാധിഷ്ഠിത വിലയിരുത്തലാണ്.","explorer":"പദ്ധതികൾ","explorer_title":"സർക്കാർ പദ്ധതികൾ","shortlist":"സംരക്ഷിച്ചത്","saved_title":"സംരക്ഷിച്ച പദ്ധതികൾ",
    },
    "bn": {
        "home":"হোম","explore":"প্রকল্প দেখুন","how":"কীভাবে কাজ করে","about":"সম্পর্কে",
        "find":"আমার প্রকল্প","find_cta":"আমার জন্য প্রকল্প খুঁজুন",
        "hero_title":"আপনার জন্য সরকারি প্রকল্প খুঁজুন",
        "hero_subtitle":"প্রয়োজন অনুযায়ী সুবিধা, বৃত্তি এবং আর্থিক সহায়তা খুঁজুন.",
        "trust":"সরকারি অফিসিয়াল পোর্টাল তথ্য","opportunities":"সুযোগ দেখুন",
        "op_title":"জীবনের প্রতিটি পর্যায়ে সরকারি সহায়তা","op_subtitle":"প্রাসঙ্গিক প্রকল্প দেখতে বিভাগ বেছে নিন.",
        "how_title":"তিনটি সহজ ধাপ","how_subtitle":"আপনার তথ্য থেকে আবেদন পথ পর্যন্ত.",
        "step1":"আপনার তথ্য দিন","step1_desc":"বয়স, রাজ্য, আয় ও বিভাগ জানান.",
        "step2":"মিলে যাওয়া প্রকল্প দেখুন","step2_desc":"আপনার তথ্য সরকারি নিয়মের সঙ্গে তুলনা করি.",
        "step3":"প্রস্তুত ও আবেদন","step3_desc":"নথি দেখে শুধু সরকারি ওয়েবসাইটে আবেদন করুন.",
        "cta_title":"প্রতি নাগরিক. প্রতি সুযোগ.","cta_subtitle":"খুঁজুন. বুঝুন. আবেদন করুন.",
        "voice_hint":"বড় লেখা ও সহজ ভাষা",
        "recommendation_profile_warning":"পরামর্শ দেখতে নিজের তথ্য পূর্ণ করুন.","go_profile":"প্রোফাইল","assessment":"প্রাথমিক মূল্যায়ন","recommended_title":"সুপারিশকৃত প্রকল্প","assessment_hint":"এটি প্রাথমিক নিয়মভিত্তিক মূল্যায়ন.","explorer":"প্রকল্প","explorer_title":"সরকারি প্রকল্প দেখুন","shortlist":"সংরক্ষিত","saved_title":"সংরক্ষিত প্রকল্প",
    },
    "mr": {
        "home":"मुख्यपृष्ठ","explore":"योजना पहा","how":"कसे कार्य करते","about":"माहिती",
        "find":"माझ्या योजना","find_cta":"माझ्यासाठी योजना शोधा",
        "hero_title":"तुमच्यासाठी सरकारी योजना शोधा",
        "hero_subtitle":"तुमच्या गरजांनुसार लाभ, शिष्यवृत्ती आणि आर्थिक मदत शोधा.",
        "trust":"अधिकृत सरकारी पोर्टलची माहिती","opportunities":"संधी पहा",
        "op_title":"जीवनाच्या प्रत्येक टप्प्यासाठी सरकारी मदत","op_subtitle":"संबंधित योजना पाहण्यासाठी विभाग निवडा.",
        "how_title":"तीन सोपे टप्पे","how_subtitle":"तुमच्या माहितीतून अर्ज मार्गापर्यंत.",
        "step1":"तुमची माहिती द्या","step1_desc":"वय, राज्य, उत्पन्न आणि वर्ग सांगा.",
        "step2":"जुळणाऱ्या योजना पहा","step2_desc":"आम्ही तुमची माहिती अधिकृत नियमांशी तपासतो.",
        "step3":"तयार करा आणि अर्ज करा","step3_desc":"कागदपत्रे तपासा आणि फक्त अधिकृत वेबसाईटवर अर्ज करा.",
        "cta_title":"प्रत्येक नागरिक. प्रत्येक संधी.","cta_subtitle":"शोधा. समजून घ्या. अर्ज करा.",
        "voice_hint":"मोठा मजकूर आणि स्पष्ट चिन्हे",
        "recommendation_profile_warning":"शिफारसी पाहण्यासाठी माहिती पूर्ण करा.","go_profile":"प्रोफाइल","assessment":"प्रारंभिक मूल्यांकन","recommended_title":"शिफारस केलेल्या योजना","assessment_hint":"हे प्रारंभिक नियमाधारित मूल्यांकन आहे.","explorer":"योजना","explorer_title":"सरकारी योजना पहा","shortlist":"जतन केलेले","saved_title":"जतन केलेल्या योजना",
    },
}


def init_language():
    if "language_name" not in st.session_state:
        st.session_state.language_name = "English"


def set_state_language(state):
    if state in STATE_LANGUAGES:
        st.session_state.language_name = STATE_LANGUAGES[state]


def t(key):
    init_language()
    code = LANGUAGES.get(st.session_state.language_name, "en")
    return TEXT.get(code, TEXT["en"]).get(key, TEXT["en"].get(key, key))


PROFILE_TEXT = {
    "en": {
        "eyebrow":"PERSONALIZED DISCOVERY","title":"Tell us about yourself",
        "hint":"Required fields are marked with *. Information stays in this session unless MongoDB is configured.",
        "category":"Beneficiary category *","student":"Student","farmer":"Farmer","business":"Business Owner",
        "job":"Job Seeker","general":"General Public","other":"Other",
        "name":"Full name","age":"Age *","gender":"Gender","gender_hide":"Prefer not to say","female":"Female","male":"Male","other_gender":"Other",
        "state":"State *","district":"District","residence":"Residence","rural":"Rural","urban":"Urban","semi":"Semi-urban","any":"Any",
        "income":"Annual family income (₹) *","education":"Education qualification","employment":"Employment status","occupation":"Occupation",
        "disability":"Disability status (only if relevant)","no":"No","yes":"Yes",
        "additional":"Additional information","documents":"Optional document upload",
        "consent":"I consent to temporary text extraction. Documents will not be permanently stored.",
        "document_type":"Document type","income_doc":"Income Certificate","community_doc":"Community Certificate","education_doc":"Educational Certificate","disability_doc":"Disability Certificate","land_doc":"Land Document",
        "upload":"Upload PDF, JPG, JPEG or PNG (maximum 5 MB)","save":"Save Profile","describe":"Or describe your profile for AI extraction","extract":"Extract with AI","submit":"Review & Submit",
        "education_level":"Current education level","course":"Course or stream","institution":"Institution type","school":"School","college":"College","university":"University","iti":"ITI/Polytechnic","academic":"Academic year",
        "farmer_status":"Farmer status","owner":"Owner cultivator","tenant":"Tenant","labourer":"Agricultural labourer","fishery":"Fishery","land_ownership":"Land ownership or tenancy","own_land":"Own land","leased":"Leased land","shared":"Shared tenancy","no_land":"No land","land_size":"Landholding size (acres)","crop":"Crop or agricultural activity",
        "business_type":"Business type","business_age":"Business age (years)","turnover":"Annual turnover (₹)","msme":"Udyam/MSME registration","unknown":"Unknown",
        "skills":"Skills","experience":"Work experience (years)",
    },
    "hi": {
        "eyebrow":"व्यक्तिगत जानकारी","title":"अपने बारे में बताएं",
        "hint":"* वाले फ़ील्ड आवश्यक हैं। MongoDB सेट होने तक जानकारी इसी सत्र में रहती है.",
        "category":"लाभार्थी श्रेणी *","student":"छात्र","farmer":"किसान","business":"व्यवसायी",
        "job":"रोजगार खोजने वाला","general":"सामान्य नागरिक","other":"अन्य",
        "name":"पूरा नाम","age":"उम्र *","gender":"लिंग","gender_hide":"बताना नहीं चाहते","female":"महिला","male":"पुरुष","other_gender":"अन्य",
        "state":"राज्य *","district":"जिला","residence":"निवास","rural":"ग्रामीण","urban":"शहरी","semi":"अर्ध-शहरी","any":"कोई भी",
        "income":"वार्षिक परिवार आय (₹) *","education":"शैक्षणिक योग्यता","employment":"रोजगार स्थिति","occupation":"व्यवसाय",
        "disability":"दिव्यांगता स्थिति (यदि लागू हो)","no":"नहीं","yes":"हाँ",
        "additional":"अतिरिक्त जानकारी","documents":"वैकल्पिक दस्तावेज़ अपलोड",
        "consent":"मैं अस्थायी पाठ निकालने की सहमति देता/देती हूं। दस्तावेज़ स्थायी रूप से नहीं रखे जाएंगे.",
        "document_type":"दस्तावेज़ का प्रकार","income_doc":"आय प्रमाणपत्र","community_doc":"जाति प्रमाणपत्र","education_doc":"शैक्षणिक प्रमाणपत्र","disability_doc":"दिव्यांगता प्रमाणपत्र","land_doc":"भूमि दस्तावेज",
        "upload":"PDF, JPG, JPEG या PNG अपलोड करें (अधिकतम 5 MB)","save":"जानकारी सुरक्षित करें","describe":"या AI के लिए अपना विवरण लिखें","extract":"AI से निकालें","submit":"समीक्षा करके जमा करें",
        "education_level":"वर्तमान शिक्षा स्तर","course":"पाठ्यक्रम या विषय","institution":"संस्था का प्रकार","school":"स्कूल","college":"कॉलेज","university":"विश्वविद्यालय","iti":"आईटीआई/पॉलिटेक्निक","academic":"शैक्षणिक वर्ष",
        "farmer_status":"किसान स्थिति","owner":"भूमि मालिक किसान","tenant":"किरायेदार","labourer":"कृषि मजदूर","fishery":"मत्स्य पालन","land_ownership":"भूमि स्वामित्व या पट्टा","own_land":"अपनी भूमि","leased":"पट्टे की भूमि","shared":"साझा पट्टा","no_land":"भूमि नहीं","land_size":"भूमि क्षेत्र (एकड़)","crop":"फसल या कृषि कार्य",
        "business_type":"व्यवसाय का प्रकार","business_age":"व्यवसाय की उम्र (वर्ष)","turnover":"वार्षिक टर्नओवर (₹)","msme":"उद्यम/MSME पंजीकरण","unknown":"पता नहीं",
        "skills":"कौशल","experience":"कार्य अनुभव (वर्ष)",
    },
    "ta": {
        "eyebrow":"தனிப்பட்ட கண்டறிதல்","title":"உங்களைப் பற்றி சொல்லுங்கள்",
        "hint":"* குறித்த பகுதிகள் கட்டாயம். MongoDB அமைக்கப்படாத வரை தகவல் இந்த அமர்வில் மட்டுமே இருக்கும்.",
        "category":"பயனாளர் வகை *","student":"மாணவர்","farmer":"உழவர்","business":"வணிக உரிமையாளர்",
        "job":"வேலை தேடுபவர்","general":"பொது மக்கள்","other":"மற்றவை",
        "name":"முழு பெயர்","age":"வயது *","gender":"பாலினம்","gender_hide":"சொல்ல விரும்பவில்லை","female":"பெண்","male":"ஆண்","other_gender":"மற்றவை",
        "state":"மாநிலம் *","district":"மாவட்டம்","residence":"குடியிருப்பு","rural":"ஊரகம்","urban":"நகரம்","semi":"அரை நகரம்","any":"எதுவும்",
        "income":"ஆண்டு குடும்ப வருமானம் (₹) *","education":"கல்வித் தகுதி","employment":"வேலை நிலை","occupation":"தொழில்",
        "disability":"ஊனமுற்றோர் நிலை (தேவைப்பட்டால் மட்டும்)","no":"இல்லை","yes":"ஆம்",
        "additional":"கூடுதல் தகவல்","documents":"விருப்ப ஆவணப் பதிவேற்றம்",
        "consent":"தற்காலிகமாக உரையைப் பிரித்தெடுக்க நான் அனுமதிக்கிறேன். ஆவணங்கள் நிரந்தரமாக சேமிக்கப்படாது.",
        "document_type":"ஆவண வகை","income_doc":"வருமானச் சான்றிதழ்","community_doc":"சமூகச் சான்றிதழ்","education_doc":"கல்வி சான்றிதழ்","disability_doc":"ஊனமுற்றோர் சான்றிதழ்","land_doc":"நில ஆவணம்",
        "upload":"PDF, JPG, JPEG அல்லது PNG பதிவேற்றம் (அதிகபட்சம் 5 MB)","save":"சுயவிவரம் சேமி","describe":"அல்லது AIக்கு சுயவிவரத்தை எழுதுங்கள்","extract":"AI மூலம் பிரித்தெடு","submit":"மதிப்பாய்வு செய்து சமர்ப்பி",
        "education_level":"தற்போதைய கல்வி நிலை","course":"பாடம் அல்லது துறை","institution":"கல்வி நிறுவனம் வகை","school":"பள்ளி","college":"கல்லூரி","university":"பல்கலைக்கழகம்","iti":"ITI/பாலிடெக்னிக்","academic":"கல்வி ஆண்டு",
        "farmer_status":"உழவர் நிலை","owner":"நில உரிமையாளர்","tenant":"குத்தகைதாரர்","labourer":"விவசாயத் தொழிலாளி","fishery":"மீன்வளம்","land_ownership":"நில உரிமை அல்லது குத்தகை","own_land":"சொந்த நிலம்","leased":"குத்தகை நிலம்","shared":"பகிர்ந்த குத்தகை","no_land":"நிலம் இல்லை","land_size":"நில அளவு (எக்கர்)","crop":"பயிர் அல்லது விவசாய செயல்பாடு",
        "business_type":"வணிக வகை","business_age":"வணிக வயது (ஆண்டுகள்)","turnover":"ஆண்டு வருவாய் (₹)","msme":"உதியம்/MSME பதிவு","unknown":"தெரியாது",
        "skills":"திறன்கள்","experience":"பணி அனுபவம் (ஆண்டுகள்)",
    },
    "te": {
        "eyebrow":"వ్యక్తిగత కనుగొనడం","title":"మీ గురించి చెప్పండి","hint":"* గుర్తున్న వివరాలు తప్పనిసరి.",
        "category":"లబ్ధిదారు వర్గం *","student":"విద్యార్థి","farmer":"రైతు","business":"వ్యాపారవేత్త","job":"ఉద్యోగ శోధకుడు","general":"సాధారణ పౌరుడు","other":"ఇతర",
        "name":"పూర్తి పేరు","age":"వయసు *","gender":"లింగం","gender_hide":"చెప్పదలచుకోలేదు","female":"మహిళ","male":"పురుషుడు","other_gender":"ఇతర",
        "state":"రాష్ట్రం *","district":"జిల్లా","residence":"నివాసం","rural":"గ్రామీణ","urban":"పట్టణ","semi":"సెమీ-అర్బన్","any":"ఏదైనా",
        "income":"సంవత్సర కుటుంబ ఆదాయం (₹) *","education":"విద్యార్హత","employment":"ఉద్యోగ స్థితి","occupation":"వృత్తి","disability":"వైకల్య స్థితి","no":"లేదు","yes":"అవును",
        "additional":"అదనపు సమాచారం","documents":"ఐచ్ఛిక పత్రాలను అప్లోడ్ చేయండి","consent":"తాత్కాలిక పాఠ్య استخراجకు నేను సమ్మతిస్తున్నాను.","document_type":"పత్ర రకం","income_doc":"ఆదాయ సర్టిఫికేట్","community_doc":"కుల సర్టిఫికేట్","education_doc":"విద్యా సర్టిఫికేట్","disability_doc":"వైకల్య సర్టిఫికేట్","land_doc":"భూమి పత్రం","upload":"PDF/JPG/JPEG/PNG అప్లోడ్ చేయండి","save":"ప్రొఫైల్ సేవ్ చేయి","describe":"AI కోసం మీ వివరాలను రాయండి","extract":"AI ద్వారా సంగ్రహించు","submit":"సమీక్ష చేసి సమర్పించు"
    },
    "kn": {
        "eyebrow":"ವೈಯಕ್ತಿಕ ಶೋಧನೆ","title":"ನಿಮ್ಮ ಬಗ್ಗೆ ತಿಳಿಸಿ","hint":"* ಗುರುತಿರುವ ಕ್ಷೇತ್ರಗಳು ಅಗತ್ಯ.",
        "category":"beneficiary ವರ್ಗ *","student":"विद्यार्थి","farmer":"ರೈತ","business":"ವ್ಯಾಪಾರಿ","job":"ಉದ್ಯೋಗ ಅನ್ವೇಷಕ","general":"ಸಾಮಾನ್ಯ ನಾಗರಿಕ","other":"ಇತರೆ",
        "name":"ಪೂರ್ಣ ಹೆಸರು","age":"ವಯಸ್ಸು *","gender":"ಲಿಂಗ","gender_hide":"ಹೇಳಲು ಇಷ್ಟವಿಲ್ಲ","female":"ಮಹಿಳೆ","male":"ಪುರುಷ","other_gender":"ಇತರೆ",
        "state":"ರಾಜ್ಯ *","district":"ಜಿಲ್ಲೆ","residence":"ನಿವಾಸ","rural":"ಗ್ರಾಮೀಣ","urban":"ನಗರ","semi":"ಅರ್ಧ-ನಗರ","any":"ಯಾವುದೇ",
        "income":"ವಾರ್ಷಿಕ ಕುಟುಂಬ ಆದಾಯ (₹) *","education":"ಶೈಕ್ಷಣಿಕ ಅರ್ಹತೆ","employment":"ಉದ್ಯೋಗ ಸ್ಥಿತಿ","occupation":"ಉದ್ಯೋಗ","disability":"ವಿಕಲಾಂಗ ಸ್ಥಿತಿ","no":"ಇಲ್ಲ","yes":"ಹೌದು",
        "additional":"ಹೆಚ್ಚುವರಿ ಮಾಹಿತಿ","documents":"ಐಚ್ಛಿಕ ದಾಖಲೆ ಅಪ್ಲೋಡ್","consent":"ತಾತ್ಕಾಲಿಕ ಪಠ್ಯ ಹೊರತೆಗೆಯಲು ನಾನು ಒಪ್ಪಿಗೆ ನೀಡುತ್ತೇನೆ.","document_type":"ದಾಖಲೆ ಪ್ರಕಾರ","income_doc":"ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ","community_doc":"ಜಾತಿ ಪ್ರಮಾಣಪತ್ರ","education_doc":"ಶೈಕ್ಷಣಿಕ ಪ್ರಮಾಣಪತ್ರ","disability_doc":"ವಿಕಲಾಂಗಿ ಪ್ರಮಾಣಪತ್ರ","land_doc":"ಭೂಮಿ ದಾಖಲೆ","upload":"PDF/JPG/JPEG/PNG ಅಪ್ಲೋಡ್","save":"ಪ್ರೊಫೈಲ್ ಉಳಿಸಿ","describe":"AIಗೆ ನಿಮ್ಮ ವಿವರವನ್ನು ಬರೆಯಿರಿ","extract":"AI ಬಳಸಿ ಹೊರತೆಗೆ","submit":"ಪರಿಶೀಲಿಸಿ ಸಲ್ಲಿಸಿ"
    },
    "ml": {
        "eyebrow":"വ്യക്തിഗത കണ്ടെത്തൽ","title":"നിങ്ങളെക്കുറിച്ച് പറയുക","hint":"* അടയാളമുള്ള ഫീൽഡുകൾ ആവശ്യമാണ്.",
        "category":"beneficiary വിഭാഗം *","student":"വിദ്യാർത്ഥി","farmer":"കർഷകൻ","business":"ബിസിനസ് ഉടമ","job":"തൊഴിൽ അന്വേഷകൻ","general":"പൊതുജനം","other":"മറ്റുള്ളത്",
        "name":"പൂർണ്ണ പേര്","age":"വയസ് *","gender":"ലിംഗഭേദം","gender_hide":"പറയാനാഗ്രഹിക്കുന്നില്ല","female":"സ്ത്രീ","male":"പുരുഷൻ","other_gender":"മറ്റുള്ളത്",
        "state":"സംസ്ഥാനം *","district":"ജില്ല","residence":"വസതി","rural":"ഗ്രാമീണ","urban":"നഗര","semi":"പകുതി നഗരം","any":"ഏതെങ്കിലും",
        "income":"വാർഷിക കുടുംബ വരുമാനം (₹) *","education":"വിദ്യാഭ്യാസയോഗ്യത","employment":"തൊഴിൽ നില","occupation":"തൊഴിൽ","disability":"വൈകല്യ നില","no":"ഇല്ല","yes":"അതെ",
        "additional":"അധിക വിവരങ്ങൾ","documents":"ഓപ്ഷണൽ ഡോക്യുമെന്റ് അപ്‌ലോഡ്","consent":"താൽക്കാലികമായി വാചകം извചകുന്നതിന് ഞാൻ സമ്മതിക്കുന്നു.","document_type":"രേഖ തരം","income_doc":"വരുമാന സർട്ടിഫിക്കറ്റ്","community_doc":"ജാതി സർട്ടിഫിക്കറ്റ്","education_doc":"വിദ്യാഭ്യാസ സർട്ടിഫിക്കറ്റ്","disability_doc":"വൈകല്യ സർട്ടിഫിക്കറ്റ്","land_doc":"ഭൂമി രേഖ","upload":"PDF/JPG/JPEG/PNG അപ്‌ലോഡ്","save":"പ്രൊഫൈൽ സംരക്ഷിക്കുക","describe":"AIയ്ക്കായി വിവരം എഴുതുക","extract":"AI ഉപയോഗിച്ച് استخراجം","submit":"പരിശോധിച്ച് സമർപ്പിക്കുക"
    },
    "bn": {
        "eyebrow":"ব্যক্তিগত অনুসন্ধান","title":"নিজের সম্পর্কে বলুন","hint":"* চিহ্নিত তথ্য আবশ্যক.",
        "category":"beneficiary বিভাগ *","student":"ছাত্র","farmer":"কৃষক","business":"ব্যবসায়ী","job":"চাকরি প্রার্থী","general":"সাধারণ নাগরিক","other":"অন্যান্য",
        "name":"পুরো নাম","age":"বয়স *","gender":"লিঙ্গ","gender_hide":"বলতে চাই না","female":"মহিলা","male":"পুরুষ","other_gender":"অন্যান্য",
        "state":"রাজ্য *","district":"জেলা","residence":"বাসস্থান","rural":"গ্রামীণ","urban":"শহর","semi":"সেমি-আরবান","any":"যেকোনো",
        "income":"বার্ষিক পরিবার আয় (₹) *","education":"শিক্ষাগত যোগ্যতা","employment":"কর্মসংস্থান অবস্থা","occupation":"পেশা","disability":"প্রতিবন্ধিতা অবস্থা","no":"না","yes":"হ্যাঁ",
        "additional":"অতিরিক্ত তথ্য","documents":"ঐচ্ছিক নথি আপলোড","consent":"অস্থায়ী text extraction-এর জন্য আমি সম্মতি দিচ্ছি.","document_type":"নথির ধরন","income_doc":"আয় সনদ","community_doc":"জাতি সনদ","education_doc":"শিক্ষা সনদ","disability_doc":"প্রতিবন্ধিতা সনদ","land_doc":"জমির নথি","upload":"PDF/JPG/JPEG/PNG আপলোড","save":"প্রোফাইল সংরক্ষণ","describe":"AI-এর জন্য নিজের বিবরণ লিখুন","extract":"AI দিয়ে বের করুন","submit":"পর্যালোচনা ও জমা"
    },
    "mr": {
        "eyebrow":"वैयक्तिक शोध","title":"आपल्या बद्दल सांगा","hint":"* चिन्हांकित माहिती आवश्यक आहे.",
        "category":"beneficiary श्रेणी *","student":"विद्यार्थी","farmer":"शेतकरी","business":"उद्योजक","job":"नोकरी शोधणारा","general":"सामान्य नागरिक","other":"इतर",
        "name":"पूर्ण नाव","age":"वय *","gender":"लिंग","gender_hide":"सांगू इच्छित नाही","female":"महिला","male":"पुरुष","other_gender":"इतर",
        "state":"राज्य *","district":"जिल्हा","residence":"निवास","rural":"ग्रामीण","urban":"शहरी","semi":"अर्ध-शहरी","any":"कोणतेही",
        "income":"वार्षिक कौटुंबिक उत्पन्न (₹) *","education":"शैक्षणिक पात्रता","employment":"रोजगार स्थिती","occupation":"व्यवसाय","disability":"दिव्यांगत्व स्थिती","no":"नाही","yes":"होय",
        "additional":"अधिक माहिती","documents":"ऐच्छिक कागदपत्र अपलोड","consent":"तात्पुरत्या मजकूर extractionसाठी मी संमती देतो.","document_type":"कागदपत्र प्रकार","income_doc":"उत्पन्न प्रमाणपत्र","community_doc":"जात प्रमाणपत्र","education_doc":"शैक्षणिक प्रमाणपत्र","disability_doc":"दिव्यांगता प्रमाणपत्र","land_doc":"जमीन दस्तऐवज","upload":"PDF/JPG/JPEG/PNG अपलोड","save":"प्रोफाइल जतन करा","describe":"AIसाठी माहिती लिहा","extract":"AIने काढा","submit":"तपासून सबमिट करा"
    },
}


def pt(key):
    init_language()
    code = LANGUAGES.get(st.session_state.language_name, "en")
    return PROFILE_TEXT.get(code, PROFILE_TEXT["en"]).get(key, PROFILE_TEXT["en"].get(key, key))
