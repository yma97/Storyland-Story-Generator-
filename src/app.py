import streamlit as st
from story_generator import StoryGenerator
import os
from dotenv import load_dotenv

# Load API key from Streamlit secrets (when deployed) or .env (when local)
try:
    # Try Streamlit secrets first (for deployment)
    api_key = st.secrets["DEEPSEEK_API_KEY"]
    os.environ["DEEPSEEK_API_KEY"] = api_key
except (KeyError, FileNotFoundError):
    # Fall back to .env file (for local development)
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")

# Verify API key exists
if not api_key:
    st.error("❌ DEEPSEEK_API_KEY not found!")
    st.info("Please add your API key to Streamlit secrets or .env file")
    st.stop()

# Page config
st.set_page_config(
    page_title="Storyland - AI Bedtime Stories",
    page_icon="🌙",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput > label, .stSelectbox > label, .stTextArea > label {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1f1f1f;
    }
    .story-box {
        background-color: #f0f7ff;
        padding: 2rem;
        border-radius: 10px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌙 Storyland")
st.subheader("AI-Powered Personalized Bedtime Stories")
st.markdown("---")

# Initialize generator
@st.cache_resource
def get_generator():
    return StoryGenerator()

try:
    generator = get_generator()
except Exception as e:
    st.error(f"❌ Failed to initialize: {e}")
    st.info("💡 Please make sure your .env file contains DEEPSEEK_API_KEY")
    st.stop()

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    story_type = st.selectbox(
        "Story Type",
        ["Regular Story", "Interactive Adventure"],
        help="Choose between a traditional story or an interactive one"
    )
    
    max_tokens = st.slider(
        "Story Length",
        min_value=300,
        max_value=2000,
        value=800,
        step=100,
        help="Longer = more detailed (and more expensive)"
    )
    
    st.markdown("---")
    st.markdown("### 📊 About")
    st.markdown("Powered by DeepSeek AI")
    st.markdown("[GitHub](https://github.com/YOUR_USERNAME/storyland)")

# Main content
col1, col2 = st.columns(2)

with col1:
    first_char_name = st.text_input(
        "First Character Name / 角色名字",
        placeholder="e.g., Guagua / 瓜瓜",
        help="Enter the first charact's name in any language"
    )

with col2:
    second_char_name = st.text_input(
        "Second Character Name / 角色名字",
        placeholder="e.g., Miemie / 咩咩",
        help="Enter the second charact's name in any language"
    )

# Theme selection
theme_options = {
    "Adventure / 冒险": "adventure",
    "Romance / 爱情": "romance",
    "Mystery / 神秘": "mystery",
    "Fantasy / 奇幻": "fantasy", 
    "Space / 太空": "space",
    "Underwater / 海洋": "underwater",
    "Forests / 森林": "forests"
}

theme_display = st.selectbox(
    "Theme / 主题",
    options=list(theme_options.keys()),
    help="Choose a theme for the story"
)
theme = theme_options[theme_display]

# Storyline input
main_storyline = st.text_input(
    "Main Storyline / 主要情节",
    placeholder="e.g., Goodnight, Star / 晚安，星星",
    help="Main storyline separated by commas (optional)"
)

# Convert storylines to list
#storylines = [i.strip() for i in main_storyline.replace('，', ',').split(',')] if main_storyline else []

st.markdown("---")

# Generate button
if st.button("✨ Generate Story / 生成故事", type="primary", use_container_width=True):
    
    # Validation
    if not first_char_name:
        st.warning("⚠️ Please enter the first charactor's name / 请输入角色一的名字")
        st.stop()
    
    if not second_char_name:
        st.warning("⚠️ Please enter the second charactor's name / 请输入角色二的名字")
        st.stop()
    
    # Generate story with progress
    with st.spinner("📖 Creating your magical story... / 正在创作您的魔法故事..."):
        try:
            # Update generator method to accept max_tokens
            story = generator.generate_story(first_char_name, second_char_name, theme, main_storyline, max_tokens)
            
            # Display story
            st.success("✅ Story generated successfully! / 故事生成成功！")
            
            st.markdown("### 📖 Your Story / 您的故事")
            st.markdown(f'<div class="story-box">{story}</div>', unsafe_allow_html=True)
            
            # Download button
            st.download_button(
                label="💾 Download Story / 下载故事",
                data=story,
                file_name=f"story_{first_char_name}_{theme}.txt",
                mime="text/plain"
            )
            
            # Save to session state for later
            if 'stories' not in st.session_state:
                st.session_state.stories = []
            
            st.session_state.stories.append({
                'first character name': first_char_name,
                'second character name': second_char_name,
                'theme': theme,
                'story': story
            })
            
        except Exception as e:
            st.error(f"❌ Error generating story: {e}")
            st.info("💡 Please check your API key and internet connection")

# Show previous stories
if 'stories' in st.session_state and st.session_state.stories:
    st.markdown("---")
    with st.expander("📚 Previously Generated Stories"):
        for i, s in enumerate(reversed(st.session_state.stories)):
            st.markdown(f"**{i+1}. {s['first character name']}** & **{s['second character name']}** - *{s['theme']}*")
            st.text(s['story'][:200] + "..." if len(s['story']) > 200 else s['story'])
            st.markdown("---")
