import flet as ft

def main(page: ft.Page):
    page.title = "Say Something App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # شريط نصي لإدخال الرسالة
    message_input = ft.TextField(label="اكتب رسالتك هنا...", width=300)

    # عنصر لعرض الرسائل المطبوعة
    output_text = ft.Text("لم يتم إرسال أي رسالة بعد.", size=16)

    def button_click(e):
        # عندما يضغط المستخدم على الزر
        if message_input.value:
            output_text.value = f"تم إرسال: {message_input.value}"
        else:
            output_text.value = "الرجاء كتابة شيء ما."
        
        # تحديث الصفحة لعرض التغيير
        page.update()

    page.add(
        ft.Column(
            [
                message_input,
                ft.ElevatedButton(text="أرسل الرسالة", on_click=button_click),
                ft.Divider(),
                output_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
