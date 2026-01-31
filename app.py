import streamlit as st
import os
import utils

# ---------------- config ----------------
st.set_page_config(
    page_title="CS Archive",
    page_icon="📚",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------- sidebar ----------------
st.sidebar.title("📁 CS Archive")

# Get sections using utility function
sections = utils.list_dirs(BASE_DIR)

# Fallback if no semesters found
if not sections:
    st.sidebar.warning("No semester folders found!")
    st.stop()

section = st.sidebar.selectbox("Select Section", sections)
section_path = os.path.join(BASE_DIR, section)

# ---------------- main ----------------
st.title(section.replace("_", " ").title())

courses = utils.list_dirs(section_path)

if not courses:
    st.info("No courses found in this section.")
else:
    for course in courses:
        # Course Expander
        with st.expander(f"📘 {course.replace('_', ' ').title()}", expanded=False):
            course_path = os.path.join(section_path, course)
            categories = utils.list_dirs(course_path)

            if not categories:
                st.caption("Empty course folder.")
                continue

            for cat in categories:
                st.markdown(f"#### 📂 {cat.replace('_', ' ').title()}")
                cat_path = os.path.join(course_path, cat)
                
                items = utils.list_files(cat_path)

                if not items:
                    st.caption("No resources available.")
                    continue

                # Grid layout for items
                for item in items:
                    item_path = os.path.join(cat_path, item)

                    # Handle Links
                    if item.endswith(".link"):
                        try:
                            with open(item_path, "r") as f:
                                url = f.read().strip()
                            st.link_button(f"🔗 {item[:-5]}", url)
                        except Exception as e:
                            st.error(f"Error reading link {item}: {e}")
                    
                    # Handle Normal Files (Download/View)
                    else:
                        with open(item_path, "rb") as f:
                            file_data = f.read()
                            
                        col1, col2 = st.columns([0.8, 0.2])
                        with col1:
                            st.text(f"📄 {item}")
                        with col2:
                            st.download_button(
                                label="⬇️ Download",
                                data=file_data,
                                file_name=item,
                                key=item_path
                            )

