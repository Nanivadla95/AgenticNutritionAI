import gradio as gr
from utils.agentic_logic import analyze_image

with gr.Blocks(title="AgenticNutritionAI 🍱") as demo:
    gr.Markdown("""
    <h1 style='text-align: center;'>🥗 AgenticNutritionAI</h1>
    <p style='text-align: center;'>Upload your meal image and get AI-powered nutrition analysis.</p>
    """)

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="📤 Upload Food Image")
            sample = gr.Examples(
                examples=[
                    "assets/pizza.jpg",
                    "assets/salad.jpg",
                    "assets/burger.jpg"
                ],
                inputs=[image_input],
                label="Try a Sample Image"
            )
            analyze_btn = gr.Button("🔍 Analyze Image")

        with gr.Column():
            image_preview = gr.Image(label="🖼️ Image Preview")
            ingredients_out = gr.Textbox(label="🍽️ Detected Ingredients", lines=1)
            nutrition_out = gr.Textbox(label="📊 Nutrition Insights", lines=5)

    analyze_btn.click(
        fn=analyze_image,
        inputs=image_input,
        outputs=[image_preview, ingredients_out, nutrition_out]
    )

demo.launch(server_name="0.0.0.0", server_port=5000)
