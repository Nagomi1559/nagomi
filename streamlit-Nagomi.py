import streamlit as st


#男女別の変換ルール
def convert_to_score(result, gender, test_type):
    if gender == "男":
        if test_type =="握力":
            if result <32:
                 return 1
            elif 37> result >= 32:
                 return 2
            elif 41>result >=37:
                 return 3
            elif 44>result >=41:
                 return 4
            elif 47>result >=44:
                 return 5
            elif 50>result >=47:
                 return 6
            elif 54>result >=50:
                 return 7
            elif 58>result >=54:
                 return 8
            elif 62>result >=58:
                 
                 return 9
            elif result >=62:
                 return 10
        elif test_type =="上体起こし":
            if result <9:
                  return 1
            elif 12>result >=9:
                 return 2
            elif 15>result >=12:
                 return 3
            elif 18>result >=15:
                 return 4
            elif 21>result >=18:
                 return 5
            elif 24>result >=21:
                 return 6
            elif 27>result >=24:
                return 7
            elif 30>result >=27:
                 return 8
            elif 33>result >=30:
                 return 9
            elif result >=33:
                 return 10
        elif test_type =="シャトルラン":
            if result <12:
                  return 1
            elif 18>result >=12:
                  return 2
            elif 24>result >=18:
                  return 3
            elif 32>result >=24:
                  return 4
            elif 43>result >=32:
                  return 5
            elif 52>result >=43:
                  return 6
            elif 67>result >=54:
                  return 7
            elif 81>result >=67:
                  return 8
            elif 95>result >=81:
                  return 9
            elif result >=95:
                  return 10
    
        elif test_type =="反復横跳び":
            if result <24:
                  return 1
            elif 31>result >=24:
                 return 2
            elif 36>result >=31:
                  return 3
            elif 41>result >=36:
                 return 4
            elif 45>result >=41:
                 return 5
            elif 49>result >=45:
              return 6
            elif 53>result >=49:
              return 7
            elif 57>result >=53:
              return 8
            elif 60>result >=57:
              return 9
            elif result >=60:
              return 10
        elif test_type =="長座体前屈":
            if result <21:
                  return 1
            elif 27>result >=21:
                    return 2
            elif 33>result >=27:
                  return 3
            elif 38>result >=33:
                return 4
            elif 43>result >=38:
                return 5
            elif 47>result >=43:
                return 6
            elif 51>result >=47:
                return 7
            elif 56>result >=51:
                return 8
            elif 61>result >=56:
                return 9
            elif result >=61:
                return 10
        elif test_type =="立ち幅跳び":
            if result <143:
                  return 1
            elif 162>result >=143:
                return 2
            elif 180>result >=162:
                return 3
            elif 195>result >=180:
                return 4
            elif 210>result >=195:
                return 5
            elif 223>result >=210:
                return 6
            elif 236>result >=223:
                return 7
            elif 248>result >=236:
                return 8
            elif 260>result >=248:
                return 9
            elif result >=260:
                return 10
             
    elif gender == "女":
        if test_type =="握力":
            if result <19:
                return 1
            elif 21>result >=19:
                return 2
            elif 24> result >=21:
                return 3
            elif 26>result >=24:
                return 4
            elif 29>result >=26:
                return 5
            elif 31>result >=29:
                 return 6
            elif 34>result >=31:
                return 7
            elif 36>result >=34:
                return 8
            elif 39>result >=36:
                return 9
            elif result >=39:
                return 10
        if test_type =="上体起こし":
            if result <1:
                return 1
            elif 5>result >=1:
                return 2
            elif 9>result >=5:
                return 3
            elif 12>result >=9:
                 return 4
            elif 15>result >=12:
                return 5
            elif 18>result >=15:
                return 6
            elif 20>result >=18:
                return 7
            elif 23>result >=20:
                return 8
            elif 25>result >=23:
                return 9
            elif result >=25:
                return 10
        elif test_type =="シャトルラン":
            if result <8:
                return 1
            elif 10>result >=8:
                return 2
            elif 14>result >=10:
                return 3
            elif 19>result >=14:
                return 4
            elif 25>result >=19:
                return 5
            elif 32>result >=25:
                return 6
            elif 41>result >=32:
                return 7
            elif 50>result >=41:
                return 8
            elif 62>result >=50:
                return 9
            elif result >=62:
                return 10
        elif test_type =="反復横跳び":
            if result <24:
                  return 1
            elif 31>result >=24:
                return 2
            elif 36>result >=31:
               return 3
            elif 41>result >=36:
                return 4
            elif 45>result >=41:
                return 5
            elif 49>result >=45:
                return 6
            elif 53>result >=49:
                return 7
            elif 57>result >=53:
                return 8
            elif 60>result >=57:
                return 9
            elif result >=60:
                return 10
        elif test_type =="長座体前屈":
            if result <21:
                  return 1
            elif 27>result >=21:
                return 2
            elif 33>result >=27:
                return 3
            elif 38>result >=33:
                return 4 
            elif 43>result >=38:
                return 5
            elif 47>result >=43:
                return 6
            elif 51>result >=47:
                return 7 
            elif 56>result >=51:
                return 8
            elif 61>result >=56:
                return 9
            elif result >=61:
                return 10
        elif test_type =="立ち幅跳び":
            if result <143:
                  return 1
            elif 162>result >=143:
                return 2
            elif 180>result >=162:
                return 3
            elif 195>result >=180:
                return 4
            elif 210>result >=195:
                return 5
            elif 223>result >=210:
                return 6
            elif 236>result >=223:
                return 7
            elif 248>result >=236:
                return 8
            elif 260>result >=248:
                return 9
            elif result >=260:
                return 10

st.title('20代の体力測定の点数')
st.write('どうも。ここでは20代の体力テストの結果を教えてもらえばその判定を出そうというアプリです（年齢の区別をつけるとめちゃくちゃやばいことになるから20歳限定にしました。悪しからず）。\nさて早速ですが自分のデータを打ち込んで見てくださいな。')
gender = st.radio('まずは性別を選択してね',["男性","女性"])

#ユーザーに体力テストの結果を入力してもらう
test_a = st.number_input("握力の結果を入力してね")
test_b = st.number_input("上体起こしの結果を入力してね")
test_c = st.number_input("シャトルランの結果を入力してね")
test_d = st.number_input("反復横跳び結果を入力してね")
test_e = st.number_input("長座体前屈の結果を入力してね")
test_f = st.number_input("立ち幅跳びの結果を入力してね")

# 各種目の結果をスコアに変換
score_a = convert_to_score(test_a, gender, "握力")
score_b = convert_to_score(test_b, gender, "上体起こし")
score_c = convert_to_score(test_c, gender, "シャトルラン")
score_d = convert_to_score(test_d, gender, "反復横跳び")
score_e = convert_to_score(test_e, gender, "長座体前屈")
score_f = convert_to_score(test_f, gender, "立ち幅跳び")

#各種目ごとの点数を表示
st.write(f"{gender}の体力テストの結果:")
st.write(f"握力の点数:{score_a}")
st.write(f"上体起こしの点数:{score_b}")
st.write(f"シャトルランの点数:{score_c}")
st.write(f"反復横跳びの点数:{score_d}")
st.write(f"長座体前屈の点数:{score_e}")
st.write(f"立ち幅跳びの点数:{score_f}")
        
#総合点数の算出
total_score = score_a + score_b + score_c + score_d + score_e + score_f 
st.write(f"総合点数:{total_score}")
def get_grade(total_score):
            if total_score >= 50:
                  return "A"
            elif 50>total_score >= 44:
                  return "B"
            elif 44>total_score >= 37:
                  return "C"
            elif 37>total_score >= 30:
                  return "D"   
            elif total_score < 30:
                  return "E"   
            
rank_score = get_grade(total_score)
st.write(f"ランク:{rank_score}")
st.write("Aだったアナタ:（50以上）人やめてない？すげえよホントに")
st.write("Bだったアナタ:（44～49）良い生活習慣してるじゃないっすか")
st.write("Cだったアナタ:（37～43）普通。それ以上でもそれ以下でもねえ")
st.write("Dだったアナタ:（30～36）まずは無理しない程度から動きましょう。")
st.write("Eだったアナタ:（30未満） 動 け 豚")
