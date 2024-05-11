import streamlit as st
import pandas as pd
import ast
import pydeck as pdk

def show_john_page():
    st.title('Urban Explorer')
    st.title('User Profile: John')
    st.write('- Lives in Philadelphia\n- Rated 6 activities\n- Average rating of 3.83\n- Enjoys a variety of activities like, sporting events, museums, and park')
    

    # Load and cache the user-specific predictions data
    @st.cache_data
    def load_user_predictions(path):
        data = pd.read_csv(path)
        return data

    # Load and cache the business data
    @st.cache_data
    def load_business_data(path):
        data = pd.read_csv(path)
        return data

    # Filter function
    def filter_predictions(predictions_df, businesses_df, open_only, categories, city, n):
        predictions_df = predictions_df.rename(columns={'iid': 'business_id', 'est': 'predicted_rating'})
        merged_df = predictions_df.merge(businesses_df, on='business_id', how='left')
        
        if open_only:
            merged_df = merged_df[merged_df['is_open'] == 1]
        if categories:
            merged_df = merged_df[merged_df['categories'].apply(lambda cats: any(cat.strip() in categories for cat in cats.split(',')))]
        if city:
            merged_df = merged_df[merged_df['city'] == city]
        
        filtered_preds = merged_df.nlargest(n, 'predicted_rating')
        final_columns = [
                'name', 'stars', 'predicted_rating', 'review_count','categories',
                'address', 'city', 'state', 'postal_code','hours', 'latitude','longitude' 
            ]
        result_df = filtered_preds[final_columns]
        
        return result_df

    # User/business file paths
    user_predictions_path = '../Data/user_predictions/john_a_predictions'
    business_data_path = '../Data/filtered_data_sets/activities.csv'

    user_predictions = load_user_predictions(user_predictions_path)
    business_data = load_business_data(business_data_path)

    # Streamlit widgets for user input
    n = st.slider('Number of top recommendations', min_value=1, max_value=50, value=10)
    cities = ['All'] + list(business_data['city'].dropna().unique())
    selected_city = st.selectbox('Select a city', options=cities)

    category_list = set([cat.strip() for sublist in business_data['categories'].dropna().str.split(',').tolist() for cat in sublist])
    selected_categories = st.multiselect('Select categories', options=['All'] + sorted(category_list))

    # Filter for 'None' if 'All' is selected
    if selected_city == 'All':
        selected_city = None
    if 'All' in selected_categories:
        selected_categories = None

    # Button to filter and display the recommendations
    if st.button('Show Recommendations'):
        result_df = filter_predictions(
            user_predictions, business_data,
            open_only=True,
            categories=selected_categories,
            city=selected_city,
            n=n
        )
        st.write(result_df)

        # ScatterplotLayer for markers
        marker_layer = pdk.Layer(
            "ScatterplotLayer",
            result_df,
            get_position="[longitude, latitude]",
            get_color="[200, 30, 0, 160]",  # RGBA color
            get_radius=75,  # Radius of the markers
        )

        # TextLayer for labels
        text_layer = pdk.Layer(
            "TextLayer",
            result_df,
            get_position="[longitude, latitude]",
            get_text="name",  # Column that contains text to display
            get_color="[255, 255, 255, 255]",  # White text
            get_size=12,
            get_alignment_baseline="'bottom'"
        )

        # Initial view state for the map
        view_state = pdk.ViewState(
            latitude=result_df['latitude'].mean(),
            longitude=result_df['longitude'].mean(),
            zoom=11,
            pitch=0
        )

        # Render the deck.gl map with both layers
        deck = pdk.Deck(
            layers=[marker_layer, text_layer],
            initial_view_state=view_state
        )

        st.pydeck_chart(deck)
