# app.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Éditeur noir-sur-noir — touche Échap", layout="wide")
st.title("Éditeur noir-sur-noir — visible uniquement quand tu maintiens la touche Échap (Esc)")

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  :root{
    --bg: #000;
    --text-hidden: #000;
    --text-visible: #fff;
    --font-size: 18px;
  }

  html,body{
    height:100%;
    margin:0;
    background:var(--bg);
    font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    -webkit-font-smoothing:antialiased;
  }

  .wrap{
    padding:16px;
    box-sizing:border-box;
  }

  textarea#editor{
    width:100%;
    height:60vh;
    resize:vertical;
    padding:12px;
    box-sizing:border-box;
    background:var(--bg);
    color:var(--text-hidden);
    caret-color:transparent;
    border: 1px solid #222;
    border-radius:8px;
    outline:none;
    font-size:var(--font-size);
    line-height:1.5;
    white-space:pre-wrap;
    overflow:auto;
  }

  textarea#editor.visible{
    color:var(--text-visible);
    caret-color:var(--text-visible);
  }

  .hint{
    margin-top:10px;
    color:#bbb;
    font-size:13px;
  }
</style>
</head>
<body>
<div class="wrap">
  <textarea id="editor" spellcheck="false" placeholder="Tape ici — le texte est invisible tant que tu ne maintiens pas Échap."></textarea>
  <div class="hint">💡 Maintiens la touche <b>Échap (Escape)</b> pour afficher temporairement ton texte.</div>
</div>

<script>
(function(){
  const editor = document.getElementById('editor');
  let escDown = false;

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !escDown) {
      escDown = true;
      editor.classList.add('visible');
      e.preventDefault(); // empêche l’effet par défaut du Esc (ex: quitter plein écran)
    }
  }, {passive:false});

  window.addEventListener('keyup', (e) => {
    if (e.key === 'Escape') {
      escDown = false;
      editor.classList.remove('visible');
    }
  }, {passive:true});

  window.addEventListener('blur', () => {
    escDown = false;
    editor.classList.remove('visible');
  });

  editor.focus();
})();
</script>
</body>
</html>
"""

components.html(html, height=600, scrolling=True)
