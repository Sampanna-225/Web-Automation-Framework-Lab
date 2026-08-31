from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

now = int(time.time())


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/") 

def CheckTitle(title: str):
    return WebDriverWait(driver , 10 ).until( #to ensure that the title is se once updated only
             EC.title_is(title)
    )

def CheckVisibility():
    return WebDriverWait(driver , 10 ).until(
                lambda d : d.execute_script("return document.readyState === 'complete';")
    )

def CheckTextBox(DQA:str , keys ):
    var = WebDriverWait(driver , 10).until(
        EC.element_to_be_clickable((By.XPATH , f"//input[@data-qa ='{DQA}']"))
    )
    var.clear()
    var.send_keys(keys)
    return var.get_attribute("value")


#Home page
is_home = CheckVisibility()

if is_home:
    print("Home Status")
    print("🟢 The document is visible ")
    login_link = WebDriverWait(driver , 10).until(
        EC.element_to_be_clickable((By.XPATH , "//a[contains(text() , ' Signup / Login')]")) # // means whole html , * means every element 
    )
    login_link.click()

    updatedTitle = False
    try:
        updatedTitle = CheckTitle("Automation Exercise - Signup / Login")

    except:
        print("⚠️ Failed Matching Title (Timeout Error || Title Mismatch)")
    
    is_signup = CheckVisibility()

    
    if updatedTitle and is_signup:
        print("🟢 SignUp button works ")
        print("")


        #Signup & Login Page
        print("Sign Up Status")
        try:
            Sign_up_page_load = CheckVisibility()
            is_NewSignup = WebDriverWait(driver , 10 ).until(
                  EC.visibility_of_element_located((By.XPATH , "//h2[contains(text() , 'New User Signup!')]"))
                  
            )
            
             
            Username_val =  CheckTextBox(DQA="signup-name" , keys="Automated Bot")
    
            Email_val = CheckTextBox(DQA="signup-email", keys=f"exampleBot{now}@gmail.com")


            print("🟢 New SignUp is Visible ")
            print(f"🟢 Username Text Box visible and {'🟢' if (Username_val =='Automated Bot') else '⚠️ Not'} Clickable")
            print(f"🟢 Email Text Box visible and {'🟢' if (Email_val == f'exampleBot{now}@gmail.com') else '⚠️ Not'} Clickable")

            Submit = WebDriverWait( driver , 10).until(
                 EC.element_to_be_clickable((By.XPATH , "//button[@data-qa = 'signup-button']"))
            )
            Submit.click()


            print("")

            # POST SUBMIT FORM
            print("Post Submit Form Status")
            try:
                post_submit_page_load = CheckVisibility()
                PSF_title = CheckTitle("Automation Exercise - Signup")
                if PSF_title:
                    try:
                        PSF_RB1 = WebDriverWait(driver , 10 ).until(
                            EC.element_to_be_clickable((By.ID , "id_gender1"))
                        )
                        PSF_RB1.click()
                            
                        #if the input comes prefilled dont and readonly dont even try it
                       
                        PSF_Pass_val = CheckTextBox(DQA="password", keys="Maf5tsf@aeds3")

                        

                        PSF_days = Select(driver.find_element(By.ID , "days"))
                        PSF_days.select_by_value("3")

                        PSF_months = Select(driver.find_element(By.ID , "months"))
                        PSF_months.select_by_value("5")#months may have value set as 1 , 2 ,3 that needs to be focused in inspect mode

                        PSF_years = Select(driver.find_element(By.ID , "years"))
                        PSF_years.select_by_value("2008")

                        checkbox1 = driver.find_element(By.ID,"newsletter")
                        checkbox1.click()

                        checkbox2 = driver.find_element(By.ID , "optin")
                        checkbox2.click()

                        driver.execute_script("window.scrollBy(0, 500);")#to scroll

                        
                        fn_val  = CheckTextBox(DQA="first_name", keys="Automated")

                        ln_val  = CheckTextBox(DQA="last_name" , keys="Bot")      

                        companu_val = CheckTextBox(DQA="company", keys="Selenium.co")      

                        address1_val = CheckTextBox(DQA="address", keys="Mumbai")            

                        address2_val = CheckTextBox(DQA="address2" , keys="Desi")

                        driver.execute_script("window.scrollBy(0,500);")# (x,y) scroll in each direction

                        state_val = CheckTextBox(DQA="state" , keys="Maharashtra")

                        city_val = CheckTextBox(DQA="city" , keys="Mumbai")

                        zip_val = CheckTextBox(DQA="zipcode" , keys="400001")

                        phone_val = CheckTextBox(DQA="mobile_number" , keys="9876543210")

                        print("🟢 Post Submit Form is Visible ")
                        print(f"🟢 Password Text Box visible and {'🟢' if (PSF_Pass_val == 'Maf5tsf@aeds3') else '⚠️ Not'} Clickable & Typable")
                        print("🟢 Dropdown Select Works Perfectly")
                        print("🟢 Checkbox works perfectlly")
                        print(f"🟢 First Name Text Box visible and {'🟢' if (fn_val == 'Automated') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 Last Name Text Box visible and {'🟢' if (ln_val == 'Bot') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 Company Text Box visible and {'🟢' if (companu_val == 'Selenium.co') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 Address 1 Text Box visible and {'🟢' if (address1_val == 'Mumbai') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 Address 2 Text Box visible and {'🟢' if (address2_val == 'Desi') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 State Text Box visible and {'🟢' if (state_val == 'Maharashtra') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 City Text Box visible and {'🟢' if (city_val == 'Mumbai') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 ZipCode Text Box visible and {'🟢' if (zip_val == '400001') else '⚠️ Not'} Clickable & Typable")
                        print(f"🟢 Mobile Number Text Box visible and {'🟢' if (phone_val == '9876543210') else '⚠️ Not'} Clickable & Typable")

                        submit = WebDriverWait(driver , 10).until(
                            EC.element_to_be_clickable((By.XPATH , "//button[@data-qa ='create-account']"))
                        )
                        submit.click()

                        print("")
                        print("Account Creation")
                        try:
                            new_acc = CheckVisibility()
                            created = WebDriverWait(driver , 10).until(
                                EC.visibility_of_element_located((By.XPATH , "//*[contains(text(),'Account Created!')]"))
                            )
                            continue_btn = WebDriverWait(driver , 10).until(
                                EC.element_to_be_clickable((By.XPATH , "//a[@data-qa = 'continue-button']"))
                            )
                            driver.execute_script("arguments[0].click();",continue_btn)#to buypass the AD overlay
                            print("🟢 Account Creation Successful")


                            try:
                                print("")
                                print("Account Deletion")
                                deletion = CheckVisibility()
                                delete_acc = WebDriverWait(driver , 10).until(
                                    EC.visibility_of_element_located((By.XPATH , "//*[contains(text(),'Delete Account')]"))
                                )
                                delete_acc.click()
                                continue_btn = WebDriverWait(driver , 10).until(
                                    EC.element_to_be_clickable((By.XPATH , "//a[@data-qa = 'continue-button']"))
                                )
                                driver.execute_script("arguments[0].click();",continue_btn)
                                print("🟢 Account Deletion Successful")
                                
                            except Exception as e:
                                print(f"⚠️ Account Deletion Error : {e}")
                        except Exception as e:
                            print(f"⚠️ The Account Created Screen has issues : {e}")


                    except Exception as e:
                        print(f"⚠️ Form elements Visibility problem || Error = {e}")
                else:
                    print("⚠️ Warning home is not visible")
            
            except:
                print("⚠️ Failed Matching Title (Timeout Error || Title Mismatch)")
            
            
            
             
        except Exception as e:
             print(f"⚠️ Form elements Visibility problem || Error = {e}")

    elif driver.title != "Automation Exercise - Signup / Login":
            print("⚠️ The link does not redirect to the SignUp page")
    elif not is_signup:
        print("⚠️ The SignUp page is not visible")
    

else:
    print("⚠️ Warning home is not visible")

driver.quit()