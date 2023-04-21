from num2words import num2words

# Hàm chuyển số thành chữ
def convert_number_to_words(number):
    return num2words(number, lang='vi')

# Sử dụng hàm
print(convert_number_to_words(12750000))
