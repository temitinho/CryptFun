import streamlit as st

# Define the function to convert text to lowercase
#text = "my name is Artemio, and i code this"
crypto_delta = 2

alphabet_list = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

alphabet_dict = {item: index for index, item in enumerate(alphabet_list)}

def encrypt_letter(letter):
    if letter in alphabet_dict.keys():
        letter_crypto_index = alphabet_dict[letter] + crypto_delta
        temp_crypto_index = letter_crypto_index % len(alphabet_list)
        letter_crypto = alphabet_list[temp_crypto_index]
        return letter_crypto
    else:
        return letter

def encrypt_text(text):
    text_encripted = ""
    for char in text:
        text_encripted +=  encrypt_letter(char)
    return f" {text_encripted} "

# Streamlit app with form
st.sidebar.title("Select Encryption delta")
crypto_delta = st.sidebar.selectbox("Choose an option", list(range(1, 27)))


def main():
    st.title("CryptoFun")
    
    # Create a form
    with st.form("text_converter_form"):
        user_input = st.text_input("Enter some text:")
        submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        result = encrypt_text(user_input)
        st.write(f"Encrypted text: **{result}**")

if __name__ == "__main__":
    main()