from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components


DEFAULT_ROOM = "LeilaESTPrepLiveClass"


def _clean_room_name(value):
    cleaned = "".join(ch for ch in value.strip() if ch.isalnum() or ch in "-_")
    return cleaned or DEFAULT_ROOM


def show_live_call():
    st.title("Live Audio / Video Call")
    st.info(
        "Use this page when you want to explain remotely. Open the same public "
        "app link on both devices, then both people enter the same room below."
    )

    room_name = st.text_input(
        "Room name",
        value=st.session_state.get("live_call_room", DEFAULT_ROOM),
        help="Use the same room name on both devices. Letters, numbers, - and _ are safest.",
    )
    room_name = _clean_room_name(room_name)
    st.session_state.live_call_room = room_name

    meet_url = f"https://meet.jit.si/{quote(room_name)}#config.prejoinPageEnabled=true"

    col1, col2 = st.columns(2)
    col1.code(meet_url, language="text")
    col2.link_button("Open Call In New Tab", meet_url, use_container_width=True)

    st.warning(
        "For camera and microphone access, use the Cloudflare HTTPS public link. "
        "Local HTTP may block media permissions in some browsers."
    )

    components.html(
        f"""
        <iframe
            src="{meet_url}"
            allow="camera; microphone; fullscreen; display-capture; autoplay"
            style="width:100%; height:min(72vh, 720px); min-height:420px; border:0; border-radius:16px;"
        ></iframe>
        """,
        height=620,
    )

    st.markdown(
        """
        **Remote use steps**

        1. Start this Streamlit app.
        2. Start the Cloudflare tunnel.
        3. Send Leila the Cloudflare public link.
        4. Both open `Live Call`.
        5. Both use the same room name.
        6. Allow camera and microphone permissions in the browser.
        """
    )
