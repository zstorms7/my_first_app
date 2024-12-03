import altair as alt
import pandas as pd
import streamlit as st

# Load the data
penguins_df = pd.read_csv('penguins.csv')

# Title and description
st.title("Zach's Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")

# Numeric feature selection
features = penguins_df.select_dtypes(include=["number"]).columns.tolist()
features = [col for col in features if col not in ['rowid', 'year']]

# Dropdown selectors for x and y variables
selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    features,
)
selected_y_var = st.selectbox(
    "What about the y?",
    features,
)

# Uncomment to allow file upload
# penguin_file = st.file_uploader("Select Your Local Penguins CSV")
# if penguin_file is not None:
#     penguins_df = pd.read_csv(penguin_file)
# else:
#     st.stop()

# Altair chart
alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(
        x=alt.X(selected_x_var, scale=alt.Scale(zero=False)),
        y=alt.Y(selected_y_var, scale=alt.Scale(zero=False)),
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
