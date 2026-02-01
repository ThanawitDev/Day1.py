total_score = 0 #เราทำกล่องเปล่าให้เก็บคะแนนรวมไว้
count = 0       #อันนี้ก็เหมือนกันแต่เราจะเอาไปนับจำนวนของนักเรียนเพื่อหาคะแนนเฉลี่ย
with open("note.txt", "r") as f: #สังให้มันเปิดไฟล์textและให้มันอ่าน
    for line in f:  #ก็ทำลูปและตั้งชื่อตัวแปรปกติ
        clean_line = line.strip()   #สร้างชื่อตัวแปรละก็ให้มันทำการตัดบรรทัดที่เกินออกโดยคำสั่งstrip
        data = clean_line.split(",")    #ให้มันแยกข้อมูล เพราะเราต้องการ int ไปคำนวณ
        
        name = data[0]  #เราแทนค่า string ด้วยdata[0]ละก็ตั้งตัวแปรให้มันชื่อnameอีกทีจะได้หยิบมาใช้ง่ายๆ
        number = int(data[1]) #เหมือนกันกับด้านบน แต่แทนเป็น integerให้คำนวณได้ 
        total_score += number #เริ่มคำนวณโดยการใช้กล่องเปล่าtotal_numberมา+=(บวกข้อมูลเรื่อยๆ)
        count += 1  #เหมือนกัน แต่เรานับสมาชิกในtext
        
        if number >= 80: #ใช้ifเฉยๆง่ายๆ
            grade = "A"
        elif number >= 50:
            grade = "B"
        else:
            grade = "F"
        
        print (f" Student: {name} | Score {number} | Grade {grade}") #แสดงผลลัพธ์ทั้งหมด เพราะงั้นต้องทำในลูปนะจ๊ะ
average_score = total_score / count #แทนค่าเฉลี่ยด้วยการเอาคะแนนที่บวกกันแล้วมาหารกับสมาชิกทั้งหมด
print(f"--- Summary ---") #แสดงผลลัพธ์
print(f"Average score for this class: {average_score}")#แสดงผลลัพธ์ของค่าเฉลี่ยที่เราแทนไว้