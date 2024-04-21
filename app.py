import streamlit as st

def generate_text_list(text1, text2):
    # Split the texts into words
    words1 = text1.split()
    words2 = text2.split()
    
    # Combine the words from both texts
    combined_words = words1 + words2
    
    # Remove duplicates
    unique_words = list(set(combined_words))
    
    return unique_words

def main():
    st.title("Text List Generator")

    # Text input fields
    text1 = st.text_input("Enter Text 1:", "")
    text2 = st.text_input("Enter Text 2:", "")

    if st.button("Generate List"):
        if text1.strip() == "" or text2.strip() == "":
            st.error("Please enter both texts.")
        else:
            output_list = generate_text_list(text1, text2)
            st.success("Unique words list generated:")
            st.write(output_list)

if __name__ == "__main__":
    main()
