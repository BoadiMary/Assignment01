customer_name = " JANE DOE "
clean_name=customer_name.strip()
lowercase_name=clean_name.lower()
titlecase_name=clean_name.title()
print("clean name:",clean_name)
print("lowercase name:",lowercase_name)
print("titlecase name:",titlecase_name)
book_title="the litle prince"
formatted_title = book_title.capitalize()
print("formatted title:",formatted_title)
product_code="bk-457-nOVEL"
uppercase_code=product_code.upper()
new_seperator_code=uppercase_code.replace('-', '/')
print("uppercase code:", uppercase_code)
print("new seperator code:",new_seperator_code)
review="This book is great. I love this book."
book_count=review.lower().count('book')
print("Book count:",book_count)
serial_number="987654321"
is_digit_only=serial_number.isdigit()
print("is digit only:",is_digit_only)
url_parts=["the", "book", "nook", "online"]
url_string= '-'.join(url_parts)
sentence_string=''.join(url_parts)
print("URL string:",url_string)
print("Sentence String:",sentence_string)
offer_code="FREESHIPPING"
is_offer_code_uppercase=offer_code.isupper()
print("is offer ode upper:",is_offer_code_uppercase)
feedback_message="I am very happy with my order!"
message_length=len(feedback_message)
print("Message Length:",message_length)