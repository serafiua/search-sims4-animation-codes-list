import streamlit as st
import re

st.title("Sims 4 Animation Codes Keyword Search")
st.markdown("**Up to Life and Death EP**")

keywords_input = st.text_input("Enter keywords (separated by space):", placeholder="e.g., clean counter")

if st.button("Search"):
    if not keywords_input.strip():
        st.warning("Please enter at least one keyword.")
    else:
        try:
            with open("Sims_4_All_Animation_Codes_Up_to_Life_and_Death.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            keywords = keywords_input.strip().split()

            pattern = re.compile(r"(?=.*" + r")(?=.*".join(map(re.escape, keywords)) + r")", re.IGNORECASE)

            results = [line.strip() for line in lines if pattern.search(line)]

            if results:
                st.success(f"Found {len(results)} result(s):")
                for i, line in enumerate(results, 1):
                    st.text(f"{i}. {line}")
            else:
                st.info("No matching results found 😢")

        except FileNotFoundError:
            st.error("Animation file not found. Make sure the .txt file is in the same folder.")
