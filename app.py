import pickle
import streamlit as st

# model = pickle.load(open('model.pkl', 'rb'))
@st.cache


def main():
    st.title('Model prediction')

    # input Variables

    # prediction code
    if st.button('Predict'):
        output = 'naxui'
        # makeprediciton = model.predict([])
        st.success(f'Idi  {output}')


if __name__ == '__main__':
    main()
