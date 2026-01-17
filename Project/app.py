"""Random Chooser - Streamlit Web App"""

import json
import random
import time
from pathlib import Path
import streamlit as st

DATA_FILE = Path(__file__).parent / "chooser_lists.json"


def load_lists() -> dict:
    """Load saved lists from file."""
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}


def save_lists(lists: dict) -> None:
    """Save lists to file."""
    DATA_FILE.write_text(json.dumps(lists, indent=2))


def get_emoji(item: str) -> str:
    """Get a relevant emoji for an item."""
    item_lower = item.lower()
    emoji_map = {
        # Food
        "pizza": "🍕",
        "burger": "🍔",
        "ramen": "🍜",
        "noodle": "🍜",
        "soup": "🍲",
        "rice": "🍚",
        "fried rice": "🍛",
        "curry": "🍛",
        "pasta": "🍝",
        "sushi": "🍣",
        "taco": "🌮",
        "chicken": "🍗",
        "tsuivan": "🍜",
        "khuushuur": "🥟",
        # Movies
        "matrix": "💊",
        "inception": "🌀",
        "pulp fiction": "💼",
        "dark knight": "🦇",
        "interstellar": "🚀",
        "parasite": "🏠",
        "spider": "🕷️",
        "shawshank": "⛓️",
        "everything everywhere": "🥯",
        "dune": "🏜️",
        # Tasks
        "clean": "🧹",
        "assignment": "📝",
        "cook": "👨‍🍳",
        "shower": "🚿",
        "friend": "👋",
        "exercise": "🏋️",
        "laundry": "🧺",
        "dishes": "🍽️",
        "subscription": "💳",
        "walk": "🚶",
    }

    for keyword, emoji in emoji_map.items():
        if keyword in item_lower:
            return emoji
    return "•"


# Page config
st.set_page_config(page_title="Random Chooser", page_icon="🎲", layout="centered")

# Custom CSS for lavender and baby pink theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFF5F9 0%, #E6E6FA 50%, #FFE4EC 100%);
    }

    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, #9B4D7C, #6B4D8A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #5C4668;
        font-style: italic;
        margin-bottom: 30px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(230, 230, 250, 0.5);
        padding: 10px;
        border-radius: 15px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #FFE4EC;
        border-radius: 10px;
        color: #4A3055;
        padding: 10px 20px;
        font-weight: 500;
    }

    .stTabs [aria-selected="true"] {
        background-color: #E6A4C4;
        color: white;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #E6A4C4, #B19CD9);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(230, 164, 196, 0.4);
    }

    .result-box {
        background: linear-gradient(135deg, #FFE4EC, #E6E6FA);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        font-size: 2rem;
        color: #3D2B4A;
        border: 3px solid #E6A4C4;
        margin: 20px 0;
        font-weight: 600;
    }

    .cute-image {
        display: block;
        margin: 0 auto;
        border-radius: 15px;
    }

    .stExpander {
        background-color: rgba(255, 228, 236, 0.5);
        border-radius: 15px;
        border: 1px solid #E6A4C4;
    }

    .spin-box {
        background: linear-gradient(135deg, #FFE4EC, #E6E6FA);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        font-size: 1.8rem;
        color: #3D2B4A;
        border: 3px solid #B19CD9;
        margin: 20px 0;
        font-weight: 600;
        animation: pulse 0.15s ease-in-out;
    }

    .final-result {
        background: linear-gradient(135deg, #FFE4EC, #E6E6FA);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        font-size: 2rem;
        color: #3D2B4A;
        border: 3px solid #E6A4C4;
        margin: 20px 0;
        font-weight: 700;
        animation: celebrate 0.5s ease-out;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    @keyframes celebrate {
        0% { transform: scale(0.8); opacity: 0; }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Header with cute image
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://em-content.zobj.net/source/apple/391/game-die_1f3b2.png", width=120)

st.markdown('<h1 class="main-header">Random Chooser</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Can\'t decide? Let fate choose for you! ✨</p>', unsafe_allow_html=True)

# Load lists
if "lists" not in st.session_state:
    st.session_state.lists = load_lists()

lists = st.session_state.lists

# Tabs for different actions
tab1, tab2, tab3 = st.tabs(["🎲 Pick Random", "📋 Manage Lists", "✨ Add Items"])

# Tab 1: Pick Random
with tab1:
    st.image("https://em-content.zobj.net/source/apple/391/crystal-ball_1f52e.png", width=80)
    st.subheader("Pick Something Random")

    if not lists:
        st.info("🌸 No lists yet! Go to 'Add Items' to create one.")
    else:
        selected_list = st.selectbox("Choose a list:", options=list(lists.keys()))

        if selected_list:
            st.write(f"**Items in '{selected_list}':**")
            for item in lists[selected_list]:
                st.write(f"{get_emoji(item)} {item}")

            if st.button("🎲 Pick Random!", type="primary", use_container_width=True):
                if lists[selected_list]:
                    items = lists[selected_list]
                    final_choice = random.choice(items)

                    # Spin animation
                    spin_placeholder = st.empty()
                    spin_emojis = ["🎰", "🎲", "🎯", "✨", "💫", "🌟"]

                    # Fast spins
                    for i in range(12):
                        display_item = random.choice(items)
                        emoji = spin_emojis[i % len(spin_emojis)]
                        spin_placeholder.markdown(
                            f'<div class="spin-box">{emoji} {display_item} {emoji}</div>',
                            unsafe_allow_html=True
                        )
                        time.sleep(0.08)

                    # Slowing down
                    for i in range(6):
                        display_item = random.choice(items)
                        emoji = spin_emojis[i % len(spin_emojis)]
                        spin_placeholder.markdown(
                            f'<div class="spin-box">{emoji} {display_item} {emoji}</div>',
                            unsafe_allow_html=True
                        )
                        time.sleep(0.15 + (i * 0.05))

                    # Final result
                    spin_placeholder.empty()
                    st.balloons()
                    st.markdown(
                        f'<div class="final-result">🌟 {final_choice} 🌟</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("This list is empty!")

# Tab 2: Manage Lists
with tab2:
    st.image("https://em-content.zobj.net/source/apple/391/card-file-box_1f5c3-fe0f.png", width=80)
    st.subheader("Your Lists")

    if not lists:
        st.info("🌸 No lists yet! Go to 'Add Items' to create one.")
    else:
        for list_name, items in lists.items():
            with st.expander(f"📋 {list_name} ({len(items)} items)"):
                for item in items:
                    col1, col2 = st.columns([4, 1])
                    col1.write(f"{get_emoji(item)} {item}")
                    if col2.button("🗑️", key=f"del_{list_name}_{item}"):
                        lists[list_name].remove(item)
                        save_lists(lists)
                        st.rerun()

                st.divider()
                if st.button(f"Delete entire '{list_name}' list", key=f"delete_{list_name}"):
                    del lists[list_name]
                    save_lists(lists)
                    st.rerun()

# Tab 3: Add Items
with tab3:
    st.image("https://em-content.zobj.net/source/apple/391/sparkles_2728.png", width=80)
    st.subheader("Add New Items")

    col1, col2 = st.columns(2)

    with col1:
        # Option to select existing list or create new
        list_options = ["➕ Create new list..."] + list(lists.keys())
        list_choice = st.selectbox("Select list:", options=list_options)

    with col2:
        if list_choice == "➕ Create new list...":
            list_name = st.text_input("New list name:")
        else:
            list_name = list_choice

    new_item = st.text_input("Item to add:")

    if st.button("Add Item ✨", type="primary"):
        if not list_name:
            st.error("Please enter a list name!")
        elif not new_item:
            st.error("Please enter an item!")
        else:
            if list_name not in lists:
                lists[list_name] = []

            if new_item in lists[list_name]:
                st.warning(f"'{new_item}' is already in '{list_name}'")
            else:
                lists[list_name].append(new_item)
                save_lists(lists)
                st.success(f"Added '{new_item}' to '{list_name}'! 🌸")
                st.rerun()

# Footer
st.divider()
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://em-content.zobj.net/source/apple/391/cherry-blossom_1f338.png", width=50)
    st.caption("Made with 💜 using Streamlit")
