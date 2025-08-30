const dotenv = require('dotenv');
const { GoogleGenerativeAI } = require('@google/generative-ai');

dotenv.config();

async function askGemini(question) {
  const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
  const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

  try {
    const result = await model.generateContent([
      {
        role: 'user',
        parts: [{ text: "You are a helpful assistant that explains Git and GitHub clearly and simply." }]
      },
      {
        role: 'user',
        parts: [{ text: question }]
      }
    ]);

    const response = result.response;
    console.log('\n💬 Gemini says:\n', response.text(), '\n');
  } catch (error) {
    console.error('❌ Error:', error.message);
  }
}

// 🧪 Try asking your first question here:
askGemini("How do I create a pull request on GitHub?");
