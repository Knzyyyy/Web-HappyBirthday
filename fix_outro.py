import re

file = r'c:\Users\USER\Music\adalah\birthday-new.html'

with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

new_para = """      <p class="outro-text reveal">
        makasih yaa udah jadi salah satu orang yang hadir dan bikin beberapa momen jadi lebih seru.<br><br>
        I'm really glad that I got to know you, walaupun mungkin awalnya kita nggak pernah nyangka bakal sampai sejauh ini jadi temen.<br><br>
        makasih juga buat semua cerita, tawa, random things, dan hal-hal kecil yang mungkin keliatannya biasa aja, tapi somehow jadi little memories worth remembering.<br>
        di umur yang baru ini, semogaa kamu makin banyak nemuin hal-hal yang bikin kamu bahagia.<br>
        I hope this year brings you more happiness, more beautiful moments, and more reasons to smile.<br><br>
        kalau nanti ada hari yang nggak sesuai sama apa yang kamu harapkan, semogaa kamu tetap kuat buat jalanin semuanya pelan-pelan.<br>
        You don't have to have everything figured out. Just keep going, one step at a time.<br>
        jangan lupa juga buat selalu apresiasi diri kamu sendiri, sekecil apa pun pencapaian kamu.<br>
        You're doing better than you think. ♡<br><br>
        semogaa semua hal baik yang kamu semogakan pelan-pelan bisa datang ke kamu.<br>
        semogaa tahun ini jadi chapter yang lebih baik, lebih tenang, dan lebih banyak cerita yang bisa kamu kenang nantinya.<br><br>
        and lastly...<br>
        thank you for being you.<br>
        makasih udah jadi kanyaaa yang aku kenal selama ini.<br>
        semogaa kita masih bisa ketawa bareng, ngobrol random, dan bikin lebih banyak cerita kecil ke depannya.<br><br>
        Once again, happy birthday, Kanyaaa. 🎂🤍<br>
        semogaa hari ini jadi salah satu hari yang kamu inget dengan senyum.<br>
        take care of yourself, keep smiling, and enjoy your new chapter.
      </p>"""

# Find the p tag start and end
pattern = r'<p class="outro-text reveal">.*?</p>'
new_content = re.sub(pattern, new_para, content, flags=re.DOTALL)

if new_content == content:
    print("ERROR: Pattern not found!")
else:
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done! Outro text updated successfully.")
