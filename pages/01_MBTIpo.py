import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 매핑
mbti_pokemon = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "description": """
        전략적이고 독립적인 성향의 INTJ는 뮤츠와 잘 어울립니다.

        - 뛰어난 지능
        - 독창적인 사고
        - 목표 지향적
        - 강한 독립성
        """
    },
    "INTP": {
        "name": "후딘",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
        "description": """
        분석적이고 호기심이 많은 INTP는 후딘과 닮았습니다.

        - 논리적 사고
        - 탐구 정신
        - 창의적 문제 해결
        - 지적 호기심
        """
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "description": """
        리더십이 강한 ENTJ는 리자몽과 잘 맞습니다.

        - 카리스마
        - 도전 정신
        - 추진력
        - 자신감
        """
    },
    "ENTP": {
        "name": "팬텀",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "description": """
        재치 있고 혁신적인 ENTP는 팬텀과 비슷합니다.

        - 창의성
        - 유머 감각
        - 아이디어 뱅크
        - 모험심
        """
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "description": """
        이상주의적이고 통찰력이 깊은 INFJ는 루기아와 어울립니다.

        - 깊은 공감 능력
        - 통찰력
        - 신념 중심
        - 배려심
        """
    },
    "INFP": {
        "name": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "description": """
        감수성이 풍부한 INFP는 이브이와 닮았습니다.

        - 상상력
        - 따뜻한 마음
        - 순수함
        - 창의성
        """
    },
    "ENFJ": {
        "name": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "description": """
        사람들을 이끄는 ENFJ는 피카츄와 잘 어울립니다.

        - 친화력
        - 리더십
        - 긍정적 에너지
        - 협동심
        """
    },
    "ENFP": {
        "name": "토게피",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
        "description": """
        밝고 자유로운 ENFP는 토게피와 비슷합니다.

        - 낙천적
        - 열정적
        - 사교적
        - 창의적
        """
    },
    "ISTJ": {
        "name": "거북왕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "description": """
        책임감이 강한 ISTJ는 거북왕과 어울립니다.

        - 신뢰성
        - 성실함
        - 꾸준함
        - 현실적 사고
        """
    },
    "ISFJ": {
        "name": "해피너스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
        "description": """
        따뜻하고 헌신적인 ISFJ는 해피너스와 닮았습니다.

        - 배려심
        - 안정감
        - 책임감
        - 친절함
        """
    },
    "ESTJ": {
        "name": "괴력몬",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
        "description": """
        조직적이고 실행력이 뛰어난 ESTJ는 괴력몬과 잘 맞습니다.

        - 강한 책임감
        - 리더십
        - 추진력
        - 현실적 판단
        """
    },
    "ESFJ": {
        "name": "푸크린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png",
        "description": """
        사교적인 ESFJ는 푸크린과 어울립니다.

        - 친절함
        - 협동심
        - 공감 능력
        - 따뜻함
        """
    },
    "ISTP": {
        "name": "루카리오",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
        "description": """
        실용적이고 침착한 ISTP는 루카리오와 닮았습니다.

        - 문제 해결 능력
        - 독립성
        - 침착함
        - 실전형 사고
        """
    },
    "ISFP": {
        "name": "나인테일",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png",
        "description": """
        예술적 감각이 뛰어난 ISFP는 나인테일과 잘 어울립니다.

        - 감성적
        - 아름다움 추구
        - 자유로운 성향
        - 온화함
        """
    },
    "ESTP": {
        "name": "초염몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "description": """
        행동력이 뛰어난 ESTP는 강력한 포켓몬과 닮았습니다.

        - 도전 정신
        - 에너지
        - 순발력
        - 모험심
        """
    },
    "ESFP": {
        "name": "파이리",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
        "description": """
        즐거움을 추구하는 ESFP는 파이리와 잘 어울립니다.

        - 활발함
        - 긍정성
        - 친화력
        - 열정
        """
    }
}

st.title("⚡ MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 알려드립니다!")

selected_mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(mbti_pokemon.keys())
)

if st.button("포켓몬 확인하기"):
    pokemon = mbti_pokemon[selected_mbti]

    st.success(f"{selected_mbti} 유형에게 추천되는 포켓몬은 **{pokemon['name']}** 입니다!")

    st.image(
        pokemon["image"],
        width=250,
        caption=pokemon["name"]
    )

    st.subheader("성격 특징")
    st.write(pokemon["description"])

    st.balloons()
