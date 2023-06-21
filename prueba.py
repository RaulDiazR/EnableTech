from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Navigate to a web page
driver.get("https://www.lipsum.com/")

# Extract the page title
page_title = driver.title
print("Page Title:", page_title)


# #Extract all a
# a_tags = driver.find_elements(By.TAG_NAME, "a")
# print("All [a] elements")

# for i in a_tags:
#     print(i.text)

# #Extract all a elements inside div class = "boxed"
# h2_elements_inside_div = driver.find_elements(By.CSS_SELECTOR, ".boxed > a")
# print("All [h2] elements inside div class Boxed")

# for i in h2_elements_inside_div:
#     print(i.text)




#Extract all a elements inside the first div
elements_inside_first_div = driver.find_elements(By.CSS_SELECTOR, "#Packages > a")
print("Nth of type")

print("Size: ")
print(len(elements_inside_first_div))

for i in elements_inside_first_div:
    print(i.text)







# #Extract all a elements inside the first div
# elements_inside_first_div = driver.find_elements(By.CSS_SELECTOR, "div")
# print("Nth of type")


# print("Size: ")
# print(len(elements_inside_first_div))

# for i in elements_inside_first_div:
#     print(i.text)



# #Extract all h2
# h2_elements = driver.find_elements(By.TAG_NAME, "h2")
# print("All [h2] elements")

# for i in h2_elements:
#     print(i.text)


# Close the WebDriver
driver.quit()