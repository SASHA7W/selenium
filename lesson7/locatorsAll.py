from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

all_courses = driver.find_element("xpath", "//a[contain(@click-event-context,'active-route router-link-exact-active btn rounded-full btn-category')]")
most_popular = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"most popular\"')]")
new_courses = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"new courses\"')]")
python = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"python\"')]")
java = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"java\"')]")
kotlinAndroid = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"kotlin_&_android\"')]")
aiEngineering = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"ai_engineering&quot\"')]")
aiCodingTools = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"ai_coding_tools\"')]")
webDev = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"web_dev\"')]")
backend = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"backend\"')]")
cloudDevops = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"cloud_&_devops\"')]")
dataScienceAnalysis = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"data_science_&_analysis\"')]")
mlMath = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"ml_&_math\"')]")
sqlDataBases = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"sql_&_databases\"')]")
goCPlusPlus = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"go_&_c++\"')]")
drafts = driver.find_element("xpath", "//a[contains(@click-event-context, '\"title\":\"drafts\"')]")
pythonDeveloper = driver.find_element("xpath", "//div[contains(@click-event-context, '\"id\":\"2\"')]")
introductionToJava = driver.find_element("xpath", "//div[contains(@click-event-context, '\"id\":\"8\"')]")
pythonFundamentals = driver.find_element("xpath", "//div[contains(@click-event-context, '\"id\":\"6\"')]")
start = driver.find_element("xpath", "/a[contains(@click-event-target, 'course-assistant-tip')]")
kotlinCore = driver.find_element("xpath", "//div[contains(@click-event-context, '\"id\":\"18\"')]")
javaBackend = driver.find_element("xpath", "//div[contains(@click-event-context, '\"id\":\"12\"')]")
introduction = driver.find_element("xpath", "//div[contains(@click-event-context, '\"id\":\"144\"')]")

languages = driver.find_element("xpath", "//span[contains(., \"fw-500 !text-white-100\")]")
pythonLink = driver.find_element("xpath", "//a[contains(@click-event-target,'Python')]")
java = driver.find_element("xpath", "//a[contains(@click-event-target,'Java')]")
kotlinAndroidLink= driver.find_element("xpath", "//a[contains(@click-event-target,'Kotlin & Android')]")
sqlAndDatabasesLink = driver.find_element("xpath", "//a[contains(@click-event-target,'SQL and Databases')]")
goAndCPlusPlusLink = driver.find_element("xpath", "//a[contains(@click-event-target,'Go & C++')]")

careerPaths = driver.find_element("xpath", "//span[contains(., \"fw-500 !text-white-100\")]")
webDevLink = driver.find_element("xpath", "//a[contains(@click-event-target,'Web Dev')]")
backend = driver.find_element("xpath", "//a[contains(@click-event-target,'Backend')]")
cloudDevopsLink = driver.find_element("xpath", "//a[contains(@click-event-target,'Cloud & DevOps')]")
dataScienceAnalysisLink = driver.find_element("xpath", "//a[contains(@click-event-target,'Data Science & Analysis')]")

subjects = driver.find_element("xpath", "//span[contains(., \"fw-500 !text-white-100\")]")
aiEngineeringLink = driver.find_element("xpath", "//a[contains(@click-event-target,'AI Engineering')]")
aiCodingToolsLink = driver.find_element("xpath", "//a[contains(@click-event-target,'AI Coding Tools')]")
mlMath = driver.find_element("xpath", "//a[contains(@click-event-target,'ML & Math')]")
earlyAccessLink = driver.find_element("xpath", "//a[contains(@click-event-target, 'Drafts')]")
fullCatalogLink = driver.find_element("xpath", "a[contains(@click-event-target, 'full_catalog')]")

resources = driver.find_element("xpath", "div[contains(@class, 'fw-500 !text-white-100')]")
blog = driver.find_element("xpath", "a[contains(@click-event-target, 'blog')]")
university = driver.find_element("xpath", "a[contains(@click-event-target, 'university')]")
guide = driver.find_element("xpath", "a[contains(@click-event-target, 'guide')]")
liveLearning = driver.find_element("xpath", "a[contains(@class, 'fw-500 !text-white-100')]")
bootcamps = driver.find_element("xpath", "a[contains(@click-event-target, 'bootcamps')]")

subscription = driver.find_element("xpath", "a[contains(@class, 'fw-500 !text-white-100')]")
forBusiness = driver.find_element("xpath", "a[contains(@click-event-target, 'for-business')]")
pricing = driver.find_element("xpath", "a[contains(@click-event-target, 'pricing')]")

hiperskill = driver.find_element("xpath", "a[contains(@class, 'fw-500 !text-white-100')]")
about = driver.find_element("xpath", "a[contains(@click-event-target, 'about')]")
careers = driver.find_element("xpath", "a[contains(@click-event-target, 'careers')]")
forContent = driver.find_element("xpath", "a[contains(@click-event-target, 'contributors')]")
creators = driver.find_element("xpath", "a[contains(@click-event-target, 'creators')]")

support = driver.find_element("xpath", "a[contains(@class, 'fw-500 !text-white-100')]")
helpCennter = driver.find_element("xpath", "a[contains(@click-event-target, 'help-center')]")
contactSupport = driver.find_element("xpath", "a[contains(@click-event-target, 'contact-support')]")
terms = driver.find_element("xpath", "a[contains(@click-event-target, 'terms')]")

googlePlay = driver.find_element("xpath", "a[contains(@click-event-target, 'googlePlay')]")
appStore = driver.find_element("xpath", "a[contains(@click-event-target, 'app-store')]")
becomeBetaTester = driver.find_element("xpath", "a[contains(@click-event-target, 'become_beta_tester')]")

hiperSkill = driver.find_element("xpath", "a[contains(@click-event-target, 'logo')]")
reddit = driver.find_element("xpath", "a[contains(@click-event-target, 'Reddit')]")
facebook = driver.find_element("xpath", "a[contains(@click-event-target, 'facebook')]")
linkdin = driver.find_element("xpath", "a[contains(@click-event-target, 'linkedin')]")
discord = driver.find_element("xpath", "a[contains(@click-event-target, 'discord')]")
instagram = driver.find_element("xpath", "a[contains(@click-event-target, 'instagram')]")
tikTok = driver.find_element("xpath", "a[contains(@click-event-target, 'tiktok')]")
YouTube = driver.find_element("xpath", "a[contains(@click-event-target, 'YouTube')]")