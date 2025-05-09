import streamlit as st
import csv
import os

# Streamlit UI
st.title("Simple CSV Input Saver")

file_name = st.text_input("Enter File Name:", "output_messages.csv")
message = st.text_area("Enter Message:")

if st.button("Save Message"):
    if file_name and message:
        # Check if the file already exists
        file_exists = os.path.isfile(file_name)

        # Open CSV file in append mode
        with open(file_name, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # If the file doesn't exist, write the header
            if not file_exists:
                writer.writerow(["Message"])

            # Write the message
            writer.writerow([message])

        st.success(f"Message saved to {file_name}")
    else:
        st.error("Please enter a file name and message!")

