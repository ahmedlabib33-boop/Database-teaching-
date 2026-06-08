from urllib.parse import quote_plus

import streamlit as st


GENRES = {
    "Study Focus": [
        "lofi study beats",
        "deep focus music",
        "ambient study music",
        "piano study music",
        "white noise for studying",
        "rain sounds study",
    ],
    "Calm": [
        "calm piano",
        "soft acoustic",
        "relaxing guitar",
        "meditation music",
        "sleepy ambient",
    ],
    "Classical": [
        "Mozart study music",
        "Beethoven piano",
        "Chopin nocturnes",
        "classical concentration music",
    ],
    "Jazz": [
        "smooth jazz",
        "coffee shop jazz",
        "jazz piano",
        "bossa nova jazz",
    ],
    "Pop": [
        "pop hits clean",
        "acoustic pop",
        "happy pop playlist",
        "soft pop study",
    ],
    "Rock": [
        "classic rock",
        "soft rock",
        "alternative rock",
        "instrumental rock",
    ],
    "Electronic": [
        "edm playlist",
        "house music",
        "techno music",
        "trance music",
        "chill electronic",
    ],
    "Hip Hop / R&B": [
        "clean hip hop playlist",
        "r&b chill",
        "lofi hip hop",
        "instrumental hip hop",
    ],
    "World Music": [
        "arabic music",
        "french music",
        "spanish music",
        "turkish music",
        "indian music",
        "korean pop",
    ],
}

MOODS = [
    "for studying",
    "for focus",
    "for relaxing",
    "for motivation",
    "instrumental",
    "clean playlist",
    "no lyrics",
]


def _music_links(query):
    encoded = quote_plus(query)
    return {
        "YouTube Music": f"https://music.youtube.com/search?q={encoded}",
        "YouTube": f"https://www.youtube.com/results?search_query={encoded}",
        "Spotify": f"https://open.spotify.com/search/{encoded}",
        "SoundCloud": f"https://soundcloud.com/search?q={encoded}",
    }


def _render_link_buttons(query):
    st.write("##### Open music search")
    links = _music_links(query)
    cols = st.columns(len(links))
    for col, (label, url) in zip(cols, links.items()):
        with col:
            st.link_button(label, url, width="stretch")


def show_music():
    st.title("Study Music Engine")
    st.write(
        "Choose a genre, mood, or custom request. The app builds direct search "
        "links so Leila can quickly find the music she wants while studying."
    )

    genre_group = st.selectbox("Music category", list(GENRES.keys()))
    genre = st.selectbox("Genre / playlist idea", GENRES[genre_group])
    mood = st.selectbox("Listening mood", MOODS)

    custom = st.text_input(
        "Custom music search",
        placeholder="Example: calm Arabic piano, French pop, rain sounds, K-pop study playlist",
    )

    query = custom.strip() if custom.strip() else f"{genre} {mood}"

    st.markdown(
        f"""
        <div style="
            margin: 1rem 0 1.5rem;
            padding: 1rem 1.25rem;
            border-radius: 16px;
            background: #f5f8ff;
            border: 1px solid #dbeafe;
        ">
            <b>Current search:</b> {query}
        </div>
        """,
        unsafe_allow_html=True,
    )

    _render_link_buttons(query)

    st.write("##### Fast genre shortcuts")
    for category, options in GENRES.items():
        with st.expander(category):
            cols = st.columns(3)
            for index, option in enumerate(options):
                with cols[index % 3]:
                    first_link = _music_links(f"{option} {mood}")["YouTube Music"]
                    st.link_button(option, first_link, width="stretch")

    st.info(
        "Tip: for studying, choose instrumental, no lyrics, lo-fi, piano, rain sounds, "
        "or white noise. These are less distracting than songs with heavy lyrics."
    )
