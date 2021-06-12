"""
token_dict
형태소 분석을 수행할 때, 거치는 전처리 과정에 필요한 여러 예외 토큰 사전
"""

"""
# 예외처리 특수 키워드: 
해당 토큰이 셋에 존재할 경우
모든 검증 과정을 스킵하고 해당 토큰들은 예외적으로 인정 
해당 단어 문서에 존재할 경우 토큰에 추가
"""
valid_words = {
    "ai", "it", "ot", "sw", "pc", "la", "cm", "op", "ed"
}

# 단일 자모음 제외셋
stop_single = {
    "ㄱ", "ㄲ", "ㄴ", 'ㄷ', "ㄸ", "ㄹ", "ㅁ", 'ㅂ', "ㅃ",
    "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ",
    "ㅎ", "ㅏ", "ㅑ", "ㅓ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ",
    "ㅜ", "ㅠ", "ㅡ", "ㅣ", "ㅔ", "ㅖ", "ㅐ", "ㅒ", "ㅟ",
    "ㅞ", "ㅚ", "ㅙ", "ㅢ",
}

"""
# 공통 부분 제거 단어 
토큰이 해당 단어로 끝날 때, 토큰에서 해당 부분만 제거
"""
endwith_remove_list = (
    "입니다", "으로", "으로서", "으로써",
    "개월", '를', '합니다', '에서', "는"
)

# 해당 단어로 끝나는 토큰을 아예 제거
stop_endwith = (
    '됬습니다', '할때면', '곘네요', '됐습니다'
)

"""
# 동일어 사전
불용어, 오타, 동의어 등으로 똑같은 의미를 내포한 경우
(동일어) -> (원본 단어)
"""
same_words = {
    '에프터이펙트':'애프터이펙트',
    '애프터이팩트':'애프터이펙트',
    '에프터이팩트':'애프터이펙트',
}

"""
#형태소 분석 예외처리
형태소 분석기의 성능으로 인해,
잘못 분해된 형태소를 재합성.
morphs와 같이 연속된 형태소의 나열이 매칭될 때,
해당 형태소들을 모두 합쳐서 word 형태소로 변환
"""
morphs_combine = {
    ('커', '스터', '마이', '징'),
    ('커', '스터', '마', '이징'),
    ('인', '플', '루', '언서'),
    ('딥', '러닝'),
    ('프로','듀', '싱'),
    ('사이언', '티스', '트'),
    ('유', '튜버'),
    ('쿠', '킹'),
    ('엔터', '테', '인', '먼', '트'),
    ('그래', '디언', '트'),
    ('그라', '디언', '트'),
    ('그레', '디언', '트'),
    ('그래디', '언', '트'),
    ('위', '빙'),
    ('귀', '요미'),
    ('덤', '벨'),
    ('스타', '일링'),
    ('카', '빙'),
    ('백', '엔드'),
    ('말', '하', '기'),
    ('듣', '기'),
    ('라', '떼'),
    ('테', '스팅'),
}

combine_lenghs = (2, 3, 4, 5)

'''
# 비속어, 무의미한 단어 필터링
'''
# TODO: 불용어 살펴보기
stop_tokens = {"이제부", '손의', '해보면', '치성', '추','징','엉','이','립','빌','첨','능','염','빠','합','밤','단', '은','직','못','해','타','젤','패','막','볼',"널","찌","쌍",'물',"암", '실과', '이프', '도', '이천칠', '데', '이외에도', '벤', '물어', '목로', '씨발', '공동으로', '아니나', '오래걸림', '엉엉', '그래', '알았어', '허', '부지', '제 외하고', '별도', '그저', '정도의', '르', '펄렁', '시작하여', '달려', '각각', '어느곳', '미리', '언젠가', '까악', '엘', '옆', '하지만', '너', '아래윗', '사이트', '그위에', '얘기', '층', '이이', '정도에', '그래서', '이전', '때', '어떻', '찹', '해주시', '대하면', '하지마', '미션', '즉', '딱', 'org', '입장에서', '보면됨', '시발년', '습니까', '말하면', '의해', '조팔', '좀', '그럼', '윤', 'ㅈㄹ', '첫번째로', '보에', '관하여', '오자마자', '해서', '오직', '아', '기반', '이내', '님', '둥둥', '쥬', '너희', '관련', '여치', '킴', '못하다하기보다는', '오히려', '조일', '아무것', '향하다', '요만큼', '기존', '보', '계', '그런지', 'qwe', '만나', '각자', '이다', '즈음하여', '사카시', '마무리', '어찌', '하진', '모', '깔고나서', '한다면', '은', '능한한', '뚫는', '더', '디', '강생', '여차', '하여금', '대해서', '언', '이건', '많아봐야', '구체', '조', '얼마큼','목이', '어느해', '환', '으로', '하면된다', '싸인', '따지지', '어떤것들', '각', '민', '마', '리지', '영', '까지도', '왜', '그러니까', '예', '후빨', '인', '아아', '내외', '할망정', '기대여', '문 강', '월초', '어', '많은', '점', '숨은요소', '힘입어', '필', '있다', 'asd', '하기', '할거', '일단', '오지', '요기', '솜', '규', '컬', '의지하여', '겸사겸사', '이르기까지', '등등', '실과', '하이', '설마', '빙', '게다가', '결론을', '양', '들면', '전후', '겁', '틀딱', '임', '아름', '티아', '요약', '안된다', '4카시', '가격어', '힘이', '당장하셈', '위하여', '쿠', '없', '못하', '더불어', '뮤지', '역대', '그렇지않으면', '했어요', '옆사람', '아니라면', '드', '본대로', '삼', '가까스로', '의외', '기점으로', '바꾸어서', '무슨', '지', '한켠으로는', '애가', '사항', '마저도', '함으로써', '해주', '이즈', '일부', '하겠는가', '추 후', '기프', '첫날', '느금', '의해되다', '따라', '이의','뒤이어', '마련', '해도', '조금', '어느때', '이용하여', '과', '흥', '미리 ', '로', 'ooo', 'rar', '찬', '포함', '쎅스', '얼마만큼', '예컨대', '결과에', 'dqz', '듯하다', '과기', '인해', '속', '제외', '툭', '이럴정도로', '이렇게', '할줄알 다', '하는바', '떼', '앞으로', '예를', '할수록', '삐걱', '자', '이유는', '덕분', '그때', 'materials', '만약', '작', '한항목', '휘익', '자체', '대해', '탕탕', '않고', '연장부', '인젠', '지든지', '예전', '그럼에도', '오로지', '부여', '하면', '이란', '받', '반대로', '버', '말할것도', '뒤', '사서', '봐', '보이', '부류의', '영차', '령','줌', '알아쳐먹게', '정이', '아니었다면', '하나', '해진', '하든지', '이상인', '할만하다', '기기', '종합한것과같이', 'x', '네', '와르르', '적', '하나에', '있', '번쨰', '이래', '와중', '수강', '최대한', '높아봐야', 'goo', '상황', '그것', '되', '기재', '근거로', '할수있어', '개새끼', '로부터', '그러', '봐야', '시부', '분간', '창녀', '특정', '애미', '지아', '스스로', '응', '시나', '치', '하게될것이다', '표', '아무도', '바로', '다', '비오 ', '과연', '리가', '저번', '위에서', '나중', '처음', '하려고하다', '하는것이', '담', '머니', '십색꺄', '저기', '안함', 'asp', '보빨', '이것', '병신', '어이', '상관', '않다면', '통해', '상단', '그런', '밑', '앞에서', '이지만', '기본', '요만한걸', '그런데', '여부', '내부', '범위', '구체적으로', '순 간', '세기', '안', '나가야', '앞', '낼', '니다', '일전', '최대', '라', '다른', '어느것', '떄문에', '해당', '전날', '내야', '이렇게말하자면', '응당', '엔', '아이구', '다다랐다가', '하기에', '하', 'ㅇㅇ', '올림', '싶', '뿐만', '들자면', '다시말하면', '놈딱', '서서', '아리', '끙끙', '어그', '둘', '조의', '이엘', '중인', '라고', '가령', '여보시오', '같', 'ㅅㅣㅋ', '잠지', '느그앰', '이렇게되면', '설령', '강인원', '시발련', '한하다', '도달하다', '족같', '임에', 'sads', '신', '콸콸', 'certified', '요', '서술한바와같이', '잡', '다시', '가서', '만약에', 'wav', '노무혐', '한곳', '이후', '나머지는', '니엄', '상주', '위주', 'xx', '그렇지만', '커스', '직접', '홍어', '무엇', '왕', '나오', '줄은모른다', '오피녀', 'l', '재발견', '을', '태', '어찌됏어 ', ' 자마자', '이천육', '의주', '강하면', '심지어', '제', '없고', '사가', '뉴', '일것이다', '하지마라', '따위', '류', '습', '곧', '한마디', '않기', '번주', '대수', '타다', '원문보기', '향해서', '따름이다', '헉', '훨씬', '차려', '고로', '졸졸', '없는', '해봐요', '네번', '예하면', '레', '급', '쳇', 'jpg', '와서', 'ly', '즉시', 'reg', '이면', '도착하다', '아이고', '이오', '아시', '씨팔','차이', '비고', 'exif', 'iii', 'net', '봉', '변경', '주', '서', '애드', '다섯 번', '않다', '되어', '이상', '도중', '토하다', '리사', '대하', '시초에', '계세', '러', '알겠는가', 'ㅁㄴㅇㄹ', 'v', '이용', '싸움', '주자', '애비', '간다', 'lv', '최종', '의', '상대', '놀라다', '바와같이', '한번쯤', '전부', ' 생각한대로', '해도된다', '여러분', '너희들', '보다더', '하도록하다', '까지', '헐떡헐떡', '퍽', '어떤', 'kr', ' 알', '아래', '장단점', '관계가', '메쓰겁다', '하는것만', '영기획', '의거', 'www', 'zz', 'com', '조로', '어제', '와아', '하도록시키다', '더욱더', '샷','다만', '구성', '뜻', '자제', '앗', '이태', '마찬가지', '나주', '어떠한', 'hudjxnarbz', '그런즉', '가도', '따르', '하하', '노마', '지장', '보아', '어찌됏든', '할바', '이천구', '싯', '양도', '월', '정도', '혹은', '리크', '어때', '더구나', '이날', 'ㅇㅈ', '파', '몰랏다', '하게하다', '쿵', '살', '가', 'co', '이만큼', 'gid', '크', '벡', '티', '무렵', '아니다', '이르다', '놓', '저', '우선', '휴', '륙', '전', '통하', '중의하나', 'mm', '저것만큼', '더욱이는', '반', '대로', '빨통', '두번째로', '삶의 질', '한데', '논하지', '제기', '십색기', '댕그', '조차', '나머지', '레스', '유', '부터', '만들', 'var', 'g', '비록', '조기', '노무현', '진짜로', '이젠', '한가지', '그만이다', '허걱', '아이쿠', '여전히', '래시', 'asdf', '미만', '저여', '레드 강', '해야한다', '여지', '까닭에', '내', '이구','흑', '대초', '구별', '역', '애', '꽈당', '아니', '보는데서', '생각이다', '연이서', '7z', '업', '일요일 아침', '틀','초반', '어보', '중단', '소인', 'z', '외에', '얼마든지', '매', '할때', '홍', '에선', '토요', '칠', '좋 아', 'idxno','어떻게', '대도', '하는', '놈현', '보드득', '사이에서', '믹', '그리하여', '체', '파다', '시반', '보고싶다', '본', '달동', '정해진', '몰라도', '마음대로', '중에서', '것', '지만', '한', '시발롬', '곳', '그러므로', '된바에야', '같다', '빠9리', '할뿐', '이유만으로', '그러면', '자기집', '결국', '아이들', '최소한', '브리', '오래','이와', '습니다', '관계없이', 'margin', '하고있었다', '따르는', 'je', '최', '답다', '자발', '쓸모', '과정', '기', '해요', '비슷하다', '반드시', '시발', '자 신', '와 ', '것들', '반면', '하기만', '요즘', '대상', '마셈', '그렇', '와이', '얼마간', '거바', '마의', '아냐', '이에', '에서', '그들', '복', '쓰여', '넷', '든간에', '여기', '보면', '운', '뚝뚝 ', 'align', '판', '이었다', '통하여', '이런', '뿐만아니라', '뿐이다', '더라도', '틀림없다', '요컨대', '또한', '따라서', '된이상', '근거하여', '핑', '부랄', '릇', '그러니', '있는계정', '하시나', '로라', '할지언정', '해도좋다', '삐걱거리다', '점에서', 'ㅎㅎ', 'ㅆ발', '북딱', '티오', '줄', '이곳', '어찌하여', '실제', 'xxx', '최근', '김에', '참조', '바꾸어말하자면', '쪽으로', '난이도', '이어서', '물건너', '오피누', '몇', '굴', '니미', '의해서', '하곤하였다', '누', '조차도', '년도', '퉤', '남들', '내면', '이봐', '앤', '그 후', '자라', '당시', '유니', '보니', '창년', 'ㅆㅂ', '니앰', '남짓', '등', '형식으로', '만큼', '않', '구토 하다', '비로소', '테이', '라이', '야', '팍', '부', '엠창', '어느', '가지', '어찌하든지', '입각하여', '얼마나', 'dbs', '한적이있다', '관이', '지금', '이미 지', '빈', '때문에', '사용', '다나', '상', '일지라도', '하구나', '망', '사까시', '무시', '여섯번', '이라면', '흐흐', '불구하고', '한방', '다음에', 'let', '나', '으', 'bit', '걸레련', '모르', '만이', '걸레년', '일때', '어떻해', '눈길', '우르르', '게', '잇따라', '펙', '줄은', '이리하여', '다섯', '까닭으로', '집', '부분', '끼', '가능은함', '린', '한때', '보빨러', '이용한', '두', '이드', '무릎쓰고','목차', '동시에', '아니라', '종일', '이 날', '례인', '관해서는', '어떤것', '주저', '보지', '위하', 'b', '끼익', '빠구리', '그치지', '경인', '지난달', '세번', '페미', '시키다', '하고', '개의치않고', '이상의', '팔', '강', '자로', '오','토', 'oval', '비길수', '하기보다는', '하자마자', '걸림', '많', '경우', '거니와', '할수있다', '따', '하물며', '를', '하셈', '제각기', '막론하고', '빙신', '비하면', '뒤따라', '푼', '라가', '신 현', '안녕하세요','대부분', '지경이다', '어쨋든', '이하', '참나', '이러이러하다', '플로', '봊', '아니면', '가야', '단어', '왜냐하면', '할지라도', '필수', '이제', '이천팔', '응디', '갖고말하자면', '리깅을', '의거하여', 'board', '하도다', '십색갸', '겨우', '우', '미니', '이', '이예', '고려하면', '윙윙', '견지에서', '마치', '보세 ', '사의', '줄거임', '이쪽', '시발새끼', '불가', '육', '좍좍', '왕이', '것과', '보세', '년', '까', '후에', '티코', '리다', '쾅쾅', '무한', '여', '항상', '종', '안뇽', '하다', '무엇때문에', '느개비', '밖에', '사', '우에', '대신', '관련이', '비추어', '걸레', '카', '닐', '아하', '혹시', '말하', '최저', '함께', '각종', '달', '한번', '쉿', '하는것도', '때문', '턱', '않도록', '구비', '나서', 'gente', '틈타', '추가', '어느쪽', '뜷려있', 'ejibl', '그리고', '이안', '괜찮아', '중', 'ttf', '숨', '내역', '해서는','프린 터', '장', '연관되다', '들', '한남', '비교적', '지잡', '오르다', 'xgob', '및', '등신', '아울러', '솨','않는다면', '누구', 'ㅅㅂ', '우리들', '이외', '매번', '대', '이때', '시키', '만은', '이렇', '거의', '붕붕', 'st', '이와같다면', '하여야', '하느니', '되다', '관계', '어디', '조가', '초고', '이기야', '휘', 'k', '존', ' 으로서', '저쪽', '그러나', '넘', '이랑', '원래', '방면으로', '하고나서', '지점', '알수', '생각하', '같은', '아무거나', '입', '제가', '안나', '모두', '할', '참', '후', '니애미', '상대적으로', '느그미', '이비', '창기', '날', '션', '비걱거리다', '하네', '사요', '위해서', 'no', '이번', '기가', '체제', '작정', '일반적으로', 'sid', '이서', '다음으로', '외에도', '이든', '만일', '로만', '구', '포', '리야', '버금', '사기전', 'ii', '잠깐', '자기', '노', '향하여', '아니나다를가', '이러한', '그동안', '요만한', '하지', '원', '그렇게', '이로', '물건너간것', '뚫려', '잘', '여유', '불 문하고', '그렇지', '이나', '안다', '지지', '다소', '좆', '론', '문의', '티에', '가자', '반은', '당일', '취소', '인하여', '그래도', '관한', '번', '당장', '동안', '만', '그러한즉', '개년', 'ci', '룻', '이렇구나', '없어', '대하여', '되는', '헉헉', '단지', '느거매', '섻스', '레이', '오호', '월요', '허허', '더군다나', '봐라', '차라리', '정', '앞의것', '느금마', '주저하지', '지말고', '싱', '건지', '많이', '보고 싶다', '하면서', 'zip', '심', '말하자면', '어기여차', '씨', '운운', '자댕이', '크기', '또', '물론', '마저', '않으면', '총적으로', '넌', '분이', '낫다', 'zxc', '실로', '무현', '저희', '어쩔수', '고맙습니다', '일', '전반', '주룩주룩', '그중에서', '같이', '바닥', '에', '애초', '다를까', '기준으로', '더 가까이', '식스', 'ik', '때가', '씹', '바꾸어말하면', '누가', '금요', '어째서', '별거', '좋', '하마터면', '아야', '그에', '하더라도', '나니', '녀', '으 로써', '로써', '남은', '가두', '마리', '하기는한데', '못하다', '잠시', 'ㅋㅋ', '수', '냄져', '프래', '없다', '바꿔', '에게',  '붕알', '저것', '보기', 'yes', '갈보', '보전깨','셋스', '명', '미치다', '주변',"welcome",'이신','오신','gb','ex','ml','vs','wi','fi','이기','th','vol','케이','우기','좋아서','pre', 'de','본적','장정','없으셔도','어로','아니야','벅차','임시','곳곳','기요','사키','않으셔도','리시',"리나",'가',"wl",'언가','지의','분나','치도',"싶으",'득',"다년간"}