import streamlit as st

st.set_page_config(
    page_title="🌟 MBTI 진로 추천기",
    page_icon="🚀",
    layout="centered"
)

st.title("🌟 MBTI 진로 추천기")
st.markdown("""
### 😎 나에게 어울리는 미래 직업은?

MBTI를 선택하면 어울리는 진로 2개를 추천해줄게!

💡 참고로 MBTI는 진로를 정하는 절대 기준이 아니라
**나를 이해하는 하나의 힌트**야!
""")

career_data = {
    "INTJ": [
        {
            "career": "🤖 AI 개발자",
            "major": "컴퓨터공학과, 인공지능학과",
            "personality": "논리적으로 생각하고 미래를 계획하는 걸 좋아하는 친구!"
        },
        {
            "career": "📊 데이터 분석가",
            "major": "통계학과, 데이터사이언스학과",
            "personality": "숫자 속에서 규칙을 찾고 문제를 해결하는 걸 즐기는 친구!"
        }
    ],
    "INTP": [
        {
            "career": "💻 소프트웨어 개발자",
            "major": "컴퓨터공학과",
            "personality": "새로운 기술과 아이디어를 탐구하는 걸 좋아하는 친구!"
        },
        {
            "career": "🔬 연구원",
            "major": "물리학과, 화학과, 생명과학과",
            "personality": "궁금한 걸 끝까지 파고드는 탐험가 같은 친구!"
        }
    ],
    "ENTJ": [
        {
            "career": "🚀 CEO·창업가",
            "major": "경영학과, 경제학과",
            "personality": "리더십이 강하고 목표를 향해 적극적으로 움직이는 친구!"
        },
        {
            "career": "📈 경영 컨설턴트",
            "major": "경영학과",
            "personality": "문제를 분석하고 해결책을 제시하는 걸 좋아하는 친구!"
        }
    ],
    "ENTP": [
        {
            "career": "💡 제품 기획자",
            "major": "경영학과, 산업공학과",
            "personality": "아이디어가 많고 새로운 걸 만드는 걸 좋아하는 친구!"
        },
        {
            "career": "📢 마케팅 전문가",
            "major": "광고홍보학과",
            "personality": "창의적인 생각으로 사람들의 관심을 끄는 데 재능 있는 친구!"
        }
    ],
    "INFJ": [
        {
            "career": "🧑‍⚕️ 심리상담사",
            "major": "심리학과",
            "personality": "다른 사람의 마음을 잘 이해하고 공감하는 친구!"
        },
        {
            "career": "✍️ 작가",
            "major": "문예창작과, 국어국문학과",
            "personality": "상상력이 풍부하고 생각을 글로 표현하는 걸 좋아하는 친구!"
        }
    ],
    "INFP": [
        {
            "career": "🎨 일러스트레이터",
            "major": "시각디자인학과",
            "personality": "감성이 풍부하고 창의력이 넘치는 친구!"
        },
        {
            "career": "📚 동화작가",
            "major": "문예창작과",
            "personality": "나만의 이야기를 만들고 표현하는 걸 좋아하는 친구!"
        }
    ],
    "ENFJ": [
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "다른 사람의 성장을 돕는 데 보람을 느끼는 친구!"
        },
        {
            "career": "🤝 인사담당자",
            "major": "경영학과",
            "personality": "사람들과 소통하고 협력하는 걸 좋아하는 친구!"
        }
    ],
    "ENFP": [
        {
            "career": "🎬 콘텐츠 크리에이터",
            "major": "미디어콘텐츠학과",
            "personality": "에너지가 넘치고 자신을 표현하는 걸 좋아하는 친구!"
        },
        {
            "career": "🎤 방송인",
            "major": "방송연예학과",
            "personality": "사람들 앞에서 이야기하는 걸 즐기는 친구!"
        }
    ],
    "ISTJ": [
        {
            "career": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "책임감이 강하고 체계적인 친구!"
        },
        {
            "career": "💰 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 정확한 일을 좋아하는 친구!"
        }
    ],
    "ISFJ": [
        {
            "career": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 다른 사람을 돕는 걸 좋아하는 친구!"
        },
        {
            "career": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "아이들과 함께 성장하는 걸 좋아하는 친구!"
        }
    ],
    "ESTJ": [
        {
            "career": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하고 책임감이 강한 친구!"
        },
        {
            "career": "🏢 기업 관리자",
            "major": "경영학과",
            "personality": "조직을 체계적으로 이끄는 데 강한 친구!"
        }
    ],
    "ESFJ": [
        {
            "career": "🏨 호텔리어",
            "major": "호텔관광학과",
            "personality": "친절하고 사람들과 어울리는 걸 좋아하는 친구!"
        },
        {
            "career": "💼 HR 전문가",
            "major": "경영학과",
            "personality": "사람을 이해하고 돕는 것을 좋아하는 친구!"
        }
    ],
    "ISTP": [
        {
            "career": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "직접 만들고 고치는 걸 좋아하는 친구!"
        },
        {
            "career": "✈️ 항공정비사",
            "major": "항공정비학과",
            "personality": "실습과 문제 해결을 좋아하는 친구!"
        }
    ],
    "ISFP": [
        {
            "career": "🎨 그래픽 디자이너",
            "major": "시각디자인학과",
            "personality": "예술적 감각이 뛰어나고 자유로운 친구!"
        },
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "순간의 아름다움을 기록하는 걸 좋아하는 친구!"
        }
    ],
    "ESTP": [
        {
            "career": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "도전을 즐기고 사람들과 쉽게 친해지는 친구!"
        },
        {
            "career": "🎙️ 스포츠 캐스터",
            "major": "미디어커뮤니케이션학과",
            "personality": "활동적이고 순발력이 뛰어난 친구!"
        }
    ],
    "ESFP": [
        {
            "career": "🎭 배우",
            "major": "연극영화과",
            "personality": "밝고 에너지가 넘치며 표현력이 풍부한 친구!"
        },
        {
            "career": "🎉 이벤트 기획자",
            "major": "관광학과, 이벤트학과",
            "personality": "재미있는 경험을 만드는 걸 좋아하는 친구!"
        }
    ]
}

mbti = st.selectbox(
    "📝 나의 MBTI를 선택해봐!",
    sorted(career_data.keys())
)

if st.button("✨ 진로 추천 받기"):
    st.success(f"🎉 {mbti} 유형에게 어울리는 진로를 소개할게!")

    for idx, job in enumerate(career_data[mbti], start=1):
        st.markdown(f"## {idx}. {job['career']}")
        st.markdown(f"🎓 **추천 학과**\n\n{job['major']}")
        st.markdown(f"💖 **이런 성격이라면 잘 맞아!**\n\n{job['personality']}")
        st.divider()

    st.balloons()

st.markdown("---")
st.info(
    "🌈 MBTI는 참고용일 뿐이야! "
    "가장 중요한 건 네가 좋아하는 것 ❤️, 잘하는 것 💪, "
    "그리고 도전해보고 싶은 것 🚀 이라는 사실을 잊지 마!"
)
