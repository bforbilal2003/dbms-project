import streamlit as st

def main():
    st.markdown(
        """
        <style>
        body {
            background-color: #02e6e2;
        }
        .header {
            color: #e68b02;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .button {
            background-color: #990000;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #00008B;
        }
        .dropdown {
            color: black;
            background-color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<p class="header">Movie Recommendation System</p>', unsafe_allow_html=True)

    genre = st.selectbox("Select Genre:", ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"], key="genre_dropdown")
    rating = st.selectbox("Select Rating:", ["PG13", "G", "PG15", "18+"], key="rating_dropdown", help="Select movie rating")
    industry = st.radio("Select Industry:", ["Hollywood", "Bollywood"], key="industry_radio")

    if st.button("Get Recommendations", key="recommend_button", help="Click to get movie recommendations"):
        recommendations = ["The Dark Knight", "Inception", "Interstellar"]  # Example recommendations
        if recommendations:
            st.markdown("**Here are your recommendations:**")
            for movie in recommendations:
                st.write(movie)
        else:
            st.error("No recommendations found for the given criteria.")

if __name__ == "__main__":
    main()
