
function searchAll() {
    const query = document.getElementById('searchInput').value;
    const resultArea = document.getElementById('results');
    resultArea.innerHTML = `
        <h3>Google</h3>
        <iframe src="https://www.google.com/search?q=${encodeURIComponent(query)}"></iframe>
        <h3>YouTube</h3>
        <iframe src="https://www.youtube.com/results?search_query=${encodeURIComponent(query)}"></iframe>
        <h3>ChatGPT</h3>
        <iframe src="https://chat.openai.com/chat?q=${encodeURIComponent(query)}"></iframe>
    `;
}

function addSlide() {
    const container = document.getElementById('slidesContainer');
    const slide = document.createElement('div');
    slide.className = 'slide';
    slide.contentEditable = true;
    slide.innerHTML = '<h3>投影片標題</h3><p>內容...</p>';
    container.appendChild(slide);
}

function generateHTML() {
    const slides = document.querySelectorAll('.slide');
    let content = '<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="UTF-8"><title>FinalYusha 簡報</title></head><body>';
    slides.forEach(s => content += `<section>${s.innerHTML}</section><hr>`);
    content += '</body></html>';
    const blob = new Blob([content], {type: 'text/html'});
    const url = URL.createObjectURL(blob);
    const link = document.getElementById('downloadLink');
    link.href = url;
    link.download = "FinalYusha.html";
    link.style.display = 'inline';
    link.innerText = "點此下載簡報";
}
