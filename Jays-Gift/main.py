import streamlit as st

# Use Streamlit's ability to render HTML and CSS
st.markdown(
    """
    <style>
    /* Set background color for Streamlit container */
    .stApp {
        background-color: #B3E5FC;  /* Light blue background */
    }

    /* Cloud animation keyframes */
    @keyframes moveClouds {
        0% {
            transform: translateX(-100%);
        }
        100% {
            transform: translateX(100%);
        }
    }

    /* Cloud styling and animation */
    .cloud {
        position: absolute;
        top: 10%;
        left: -200px;
        width: 200px;
        height: 100px;
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/036/395/794/small/blue-sky-cloud-bubble-pixel-design-for-decoration-wheather-forcast-pixel-design-png.png'); /* Cloud image */
        background-size: contain;
        background-repeat: no-repeat;
        animation: moveClouds 30s linear infinite; /* 30-second infinite animation */
    }

    .cloud2 {
        position: absolute;
        top: 30%;
        left: -300px;
        width: 150px;
        height: 75px;
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/036/395/794/small/blue-sky-cloud-bubble-pixel-design-for-decoration-wheather-forcast-pixel-design-png.png');
        background-size: contain;
        background-repeat: no-repeat;
        animation: moveClouds 40s linear infinite; /* Slightly different timing */
    }

    .cloud3 {
        position: absolute;
        top: 50%;
        left: -400px;
        width: 250px;
        height: 125px;
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/036/395/794/small/blue-sky-cloud-bubble-pixel-design-for-decoration-wheather-forcast-pixel-design-png.png');
        background-size: contain;
        background-repeat: no-repeat;
        animation: moveClouds 50s linear infinite;
    }

    /* Added cloud4 */
    .cloud4 {
        position: absolute;
        top: 70%;
        left: -500px;
        width: 200px;
        height: 100px;
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/036/395/794/small/blue-sky-cloud-bubble-pixel-design-for-decoration-wheather-forcast-pixel-design-png.png');
        background-size: contain;
        background-repeat: no-repeat;
        animation: moveClouds 60s linear infinite; /* Slightly different timing */
    }

    /* Added cloud5 */
    .cloud5 {
        position: absolute;
        top: 90%;
        left: -600px;
        width: 300px;
        height: 150px;
        background-image: url('https://static.vecteezy.com/system/resources/thumbnails/036/395/794/small/blue-sky-cloud-bubble-pixel-design-for-decoration-wheather-forcast-pixel-design-png.png');
        background-size: contain;
        background-repeat: no-repeat;
        animation: moveClouds 70s linear infinite;
    }

    </style>

    <div class="cloud"></div>
    <div class="cloud2"></div>
    <div class="cloud3"></div>
    <div class="cloud4"></div>
    <div class="cloud5"></div>
    """, unsafe_allow_html=True
)

import streamlit as st

# Embed YouTube audio (hidden player) to play music once when the app loads
st.markdown(
    """
    <iframe width="0" height="0" src="https://www.youtube.com/embed/PuMz4v5PYKc?autoplay=1&loop=1&playlist=PuMz4v5PYKc" 
    frameborder="0" allow="autoplay" allowfullscreen></iframe>
    """, unsafe_allow_html=True
)

# Initialize session state to track button clicks
if 'click_me_clicked' not in st.session_state:
    st.session_state.click_me_clicked = False
if 'sweet_memory_clicked' not in st.session_state:
    st.session_state.sweet_memory_clicked = False
if 'what_i_love_clicked' not in st.session_state:
    st.session_state.what_i_love_clicked = False
if 'a_wish_clicked' not in st.session_state:
    st.session_state.a_wish_clicked = False
if 'a_reminder_clicked' not in st.session_state:
    st.session_state.a_reminder_clicked = False
if 'see_you_soon_clicked' not in st.session_state:
    st.session_state.see_you_soon_clicked = False

# Title of the app
st.title("🎉 Happy Birthday, Jay! 🎂")

# Subheader with a special message
st.subheader("A little surprise, just for you 🩵")

# Display a Cinnamoroll-themed image
st.image("https://i.pinimg.com/originals/87/28/6c/87286c41e6ef755e149e64f99ce1d269.gif")

# Add an interactive text input box
partner_name = st.text_input("What's your name?:", "")

# Add the first button that displays a special message when clicked
if st.button("Click Me! :3") or st.session_state.click_me_clicked:
    if partner_name.strip():  # Ensure name is not empty or just spaces
        st.session_state.click_me_clicked = True
        # Display the birthday message
        st.write(f"🩵 Dear {partner_name}, Happy Birthday to my favorite person in the world! 🎉")
        st.write("I love you more than the sun loves the moon")
    else:
        st.write("Oops! Please type your name to get your birthday message.")

    # Show the next button only after the first button is clicked and name is entered
    if st.session_state.click_me_clicked:
        if st.button("A Sweet Memory") or st.session_state.sweet_memory_clicked:
            st.session_state.sweet_memory_clicked = True
            st.write("Holding you as you sleep on the train, your sweet scent, in that moment, everything felt right, I long to hold you like that again, my beautiful boy")

            # Show the next button after "A Sweet Memory" is clicked
            if st.button("What I love") or st.session_state.what_i_love_clicked:
                st.session_state.what_i_love_clicked = True
                st.write("I love the way you care for others, your consideration, the way you see me in everything, your love, your smile, your laughter, your kindness, and ultimately... I love you")

                # Show the next button after "What I love" is clicked
                if st.button("A Wish") or st.session_state.a_wish_clicked:
                    st.session_state.a_wish_clicked = True
                    st.write("I wish the moon, the stars, the sun, and the ocean for you. Ur deserving of the whole universe, my stunning stardust. Most of all, I wish I could be there with you, but even when far, look up at the sky and remember I'm always by your side.")

                    # Show the next button after "A Wish" is clicked
                    if st.button("A Reminder!") or st.session_state.a_reminder_clicked:
                        st.session_state.a_reminder_clicked = True
                        st.write("Mi amor, te amo, I want you to know that although life is unexpected and overwhelming, you'll never have to face it alone, I'll be by your side, just like you'd be on mine. My soul mate, we'll get through anything and everything together.")

                        # Show the last button after "A Reminder!" is clicked
                        if 'happy_birthday_clicked' not in st.session_state:
                            st.session_state.happy_birthday_clicked = False

                        # Inside the final "See you soon!" button logic
                        if st.button("See you soon!") or st.session_state.see_you_soon_clicked:
                            st.session_state.see_you_soon_clicked = True
                            st.write("I can't wait, I'll hold you close, kiss you softly, and swing you around when you jump at me this time. I'll see you soon my pretty kitty, te adoro.")

                            # Separate control for the final "Happy Birthday!" button
                            if st.button("Happy Birthday!") or st.session_state.happy_birthday_clicked:
                                st.session_state.happy_birthday_clicked = True
                                st.write("I know birthdays aren't always easy, but I hope I can make this one a little bit more special for you. Happy Birthday, Jay 🩵")


# Add a GIF to the bottom of the page with a custom-styled caption
st.image(
    "https://cutekawaiiresources.wordpress.com/wp-content/uploads/2016/11/cinnamoroll-1-foot.gif",
    width=600  # You can adjust the width here
)

# Add a larger, more visible caption using HTML and CSS
st.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-size: 24px; font-weight: bold; color: #FFFFFF;'>I LOVE YOU KITTY!!!!!! 💙💙💙💙💙</p>
    </div>
    """, unsafe_allow_html=True
)

