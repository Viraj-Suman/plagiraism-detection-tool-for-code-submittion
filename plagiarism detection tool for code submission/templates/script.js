const clearBtn = document.getElementById('clearBtn');
const code1Textarea = document.getElementById('code1');
const code2Textarea = document.getElementById('code2');
const resultDiv = document.getElementById('result');

if (clearBtn) {
  clearBtn.addEventListener('click', () => {
    // Clear textareas
    code1Textarea.value = '';
    code2Textarea.value = '';
    
    // Clear result if it exists
    if (resultDiv) {
      resultDiv.remove();
    }
    
    // Reset language selectors
    const languageSelectors = document.querySelectorAll('.language-selector');
    languageSelectors.forEach(selector => {
      selector.value = 'Auto-detect';
    });
  });
}