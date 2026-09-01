# Libraries
import os,re, json,argparse,requests                # Interact with os, Regular Expressions, Encode/Decode Json Data, Parse Command-line argument and Make HTTP Request respectively
from bs4 import BeautifulSoup                       # Main class from bs4 to parse HTML or XML
from dotenv import load_dotenv                      # Used for loading data from .env
import google.generativeai as genai                 # Python package for Google Gemini Models

# Import Gemini key from Enviornment variables 
def load_key()->str:                                # Load Key from .env function and returns a string
    load_dotenv()                                   # Load the .env file
    k=os.getenv("GEMINI_API_KEY")                   # Extract Gemini Key
    if not k:                                       # If not present then raise error
        raise SystemExit("Set Appropriate Gemini Key in .env")
    return k                                        # Return key

# Webpage cleaner
def fetch_clean(url:str,timeout:int=20)->tuple[str,str]:                # Function that downloads webpage and extract information and store in form of tuple(title,text)
    r=requests.get(url,timeout=timeout,headers={                        # Downloads the webpage, sends HTTPS GET request
        "User-Agent":"Mozilla/5.0 (Summarizer)",                        # Use Custom User-Agent so server treats like a browser
        "Accept-Language":"en",
    })
    r.raise_for_status()                                                # Stop program if request fails
    soup=BeautifulSoup(r.text,"html.parser")                            # Turn raw HTML into structured object for easy navigation
    title=(soup.title.string or "").strip() if soup.title else ""       # Extract Title from <title> tag
    # Remove Non-readable tags
    for tag in soup(["script","noscript","header","footer","nav","aside","form","svg","img","video","audio","iframe","canvas"]):
        tag.decompose()
    # Collect meaningful information
    parts=[]
    for t in soup.find_all(["h1","h2","h3","p","li","blockquote"]):
        txt=t.get_text(" ",strip=True)
        if txt and len(txt.split())>=3: parts.append(txt)
    text=re.sub(r"\s+"," ","\n".join(parts)).strip()
    if not text:
        raise SystemExit("Could Not Extract Readable Text")
    return title,text

# Convert to Smaller Chunks
def chunks(s:str,n:int=12000,overlap:int=400):
    if len(s)<=n:yield s; return
    i=0
    while i<len(s):
        seg=s[i:i+n]
        j=seg.rfind("\n")
        if j>n*0.6:seg=seg[:j]
        yield seg
        i+=max(1,len(seg)-overlap)

# Model 
def make_model(model_name="gemini-2.5-flash"):
    genai.configure(api_key=load_key())
    try:
        return genai.GenerativeModel(model_name,generation_config={"response_mime_type":"application/json"})
    except Exception:
        return genai.GenerativeModel(model_name)

def parse_json(s:str)->dict:
    try:
        return json.loads(s)
    except Exception:
        m=re.search(r"```json\s*({.*?\})\s*```",s,re,s) or re.search(r"(\{.*\})",s,re.S)
        if m:
            try: return json.loads(m.group(1))
            except Exception:pass
        return {"abstract":s.strip(),"bullets":[]}
    