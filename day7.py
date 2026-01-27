salaries_list = [3000, 4000, 2500, 5000] #ข้อมูลที่มี


def total_payout(all_salaries):            #สร้างชุดคำสั่ง
    total = 0                               #สร้างกล่องเปล่า
    for salary in all_salaries :            #ให้เงินเดือนในเงินเดือนทั้งหมด
        total += salary                     #เอาเงินมาใส่ในกล่องเรื่อยๆจนหมด
    return total                            #วิ่งกลับไปบอกกล่องว่าได้เงินเดือนาทั้งหมดเท่าไหร่


final_budget = total_payout(salaries_list)  #สร้างตัวแปรว่า เงินเดือนครั้งสุดท้ายคือเงินทั้งหมดที่ต้องจ่ายในsalaries listที่total_payoutไปคำนวมาให้
print (f"All salaries budget is {final_budget}")    #ประกาศข้อมูลทั้งหมด
