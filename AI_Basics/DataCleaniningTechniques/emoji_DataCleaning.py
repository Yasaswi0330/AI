import re

text = """ ⭐⭐⭐⭐⭐ Great experience! The service was smooth, professional, and exceeded my expectations.
 😊👏 Highly recommended for anyone looking for quality and reliability! 🚀✨"""

cleaned_text = re.sub(r'[^\x00-\x7f]+', '',text)

print(cleaned_text)