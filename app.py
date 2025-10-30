# app.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Éditeur noir-sur-noir — affiche quand tu appuies", layout="wide")
st.title("Éditeur noir-sur-noir — visible **seulement** quand tu appuies sur une touche")

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  :root{
    --bg: #000;        /* fond noir */
    --text-hidden: #000; /* texte caché (noir sur noir) */
    --text-visible: #fff; /* texte visible (blanc) */
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
    color:var(--text-hidden); /* texte invisible par défaut (noir) */
    caret-color:transparent; /* caret invisible par défaut */
    border: 1px solid #222;
    border-radius:8px;
    outline:none;
    font-size:var(--font-size);
    line-height:1.5;
    white-space:pre-wrap;
    overflow:auto;
  }

  /* Quand la classe .visible est présente : texte et caret deviennent visibles */
  textarea#editor.visible{
    color:var(--text-visible);
    caret-color:var(--text-visible);
  }

  /* placeholder gris (mais pas très visible sur fond noir) */
  textarea#editor::placeholder{
    color:#222;
  }

  .hint{
    margin-top:10px;
    color:#bbb;
    font-size:13px;
  }

  /* pour que la sélection ne révèle pas trop en dehors du comportement (optionnel) */
  textarea#editor::selection{
    background:#444;
  }
</style>
</head>
<body>
<div class="wrap">
  <textarea id="editor" spellcheck="false" placeholder="Tape ici — le texte est invisible tant que tu ne presses pas de touche."></textarea>
  <div class="hint">Le texte s'affiche uniquement **lorsque une (ou plusieurs) touche(s)** est (sont) maintenue(s) ; quand il n'y a plus de touche appuyée, le contenu redevient invisible.</div>
</div>

<script>
(function(){
  const editor = document.getElementById('editor');

  // Set pour tracker quelles touches sont maintenues
  const downKeys = new Set();

  // Événements globaux pour capter keydown/keyup même si la zone perd le focus
  window.addEventListener('keydown', (e) => {
    // On ignore les touches de modification seules si besoin, mais pour l'instant tout déclenche
    downKeys.add(e.code || e.key);
    if (downKeys.size > 0) {
      editor.classList.add('visible');
    }
  }, {passive:true});

  window.addEventListener('keyup', (e) => {
    downKeys.delete(e.code || e.key);
    if (downKeys.size === 0) {
      editor.classList.remove('visible');
    }
  }, {passive:true});

  // Si la fenêtre perd le focus (ex: alt-tab), on nettoie l'état
  window.addEventListener('blur', () => {
    downKeys.clear();
    editor.classList.remove('visible');
  });

  // lorsque le texte est collé, on peut vouloir qu'il reste invisible jusqu'à appui
  editor.addEventListener('paste', () => {
    // pas d'action : collé reste invisible
  });

  // Pour meilleure UX : focus automatique sur la zone
  editor.focus();

  // Optionnel : empêcher que Ctrl/Meta+key déclenche les raccourcis du navigateur
  // (décommenter si tu veux bloquer certains raccourcis)
  /*
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 's') {
      e.preventDefault();
    }
  });
  */
})();
</script>
</body>
</html>
"""

components.html(html, height=600, scrolling=True)
