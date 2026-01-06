// Game JavaScript for enhanced UX
document.addEventListener('DOMContentLoaded', function() {
    const guessForm = document.getElementById('guess-form');
    const guessInput = document.getElementById('guess');
    const submitBtn = document.getElementById('submit-btn');
    const resetBtn = document.getElementById('reset-btn');
    const messageDiv = document.getElementById('message');

    // Input validation and enhancement
    guessInput.addEventListener('input', function() {
        const value = parseInt(this.value);
        const isValid = value >= 1 && value <= 100 && !isNaN(value);

        if (this.value === '') {
            this.classList.remove('error');
            submitBtn.disabled = false;
        } else if (!isValid) {
            this.classList.add('error');
            submitBtn.disabled = true;
        } else {
            this.classList.remove('error');
            submitBtn.disabled = false;
        }
    });

    // Enter key support
    guessInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !submitBtn.disabled) {
            guessForm.dispatchEvent(new Event('submit'));
        }
    });

    // Form submission with loading state
    guessForm.addEventListener('submit', function(e) {
        const value = parseInt(guessInput.value);
        if (value < 1 || value > 100 || isNaN(value)) {
            e.preventDefault();
            showError('Veuillez entrer un nombre entre 1 et 100');
            guessInput.focus();
            return;
        }

        // Add loading state
        submitBtn.classList.add('loading');
        submitBtn.innerHTML = '<i class="fas fa-spinner"></i><span class="btn-text">Vérification...</span>';
        submitBtn.disabled = true;
    });

    // Reset button functionality
    resetBtn.addEventListener('click', function() {
        if (confirm('Voulez-vous vraiment commencer une nouvelle partie ?')) {
            // Clear session by making a request to reset endpoint
            fetch('/reset', { method: 'POST' })
                .then(() => {
                    location.reload();
                })
                .catch(() => {
                    // Fallback: reload page
                    location.reload();
                });
        }
    });

    // Message animations
    function showError(message) {
        messageDiv.innerHTML = `<div class="message-content error">${message}</div>`;
        messageDiv.classList.add('error');
        setTimeout(() => {
            messageDiv.classList.remove('error');
        }, 500);
    }

    function showSuccess(message) {
        messageDiv.innerHTML = `<div class="message-content success">${message}</div>`;
        messageDiv.classList.add('success');
        setTimeout(() => {
            messageDiv.classList.remove('success');
        }, 600);
    }

    // Auto-focus input on page load
    guessInput.focus();

    // Touch device optimizations
    if ('ontouchstart' in window) {
        // Prevent zoom on input focus on iOS
        guessInput.addEventListener('focus', function() {
            this.setAttribute('readonly', 'readonly');
            setTimeout(() => {
                this.removeAttribute('readonly');
                this.focus();
            }, 100);
        });
    }

    // Service Worker registration for PWA capabilities
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            // Note: Service worker would need to be implemented for full PWA
            // navigator.serviceWorker.register('/sw.js');
        });
    }

    // Keyboard navigation improvements
    document.addEventListener('keydown', function(e) {
        // Escape key to clear input
        if (e.key === 'Escape') {
            guessInput.value = '';
            guessInput.focus();
        }

        // Ctrl/Cmd + Enter to submit
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter' && !submitBtn.disabled) {
            guessForm.dispatchEvent(new Event('submit'));
        }
    });

    // Visual feedback for button interactions
    submitBtn.addEventListener('mousedown', function() {
        this.style.transform = 'scale(0.98)';
    });

    submitBtn.addEventListener('mouseup', function() {
        this.style.transform = '';
    });

    submitBtn.addEventListener('mouseleave', function() {
        this.style.transform = '';
    });

    // Dynamic message updates
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList' && mutation.target === messageDiv) {
                // Add entrance animation to new messages
                const newContent = messageDiv.querySelector('.message-content');
                if (newContent) {
                    newContent.style.animation = 'none';
                    setTimeout(() => {
                        newContent.style.animation = '';
                    }, 10);
                }
            }
        });
    });

    observer.observe(messageDiv, { childList: true });

    // Performance optimization: Debounce input validation
    let validationTimeout;
    function debounceValidation() {
        clearTimeout(validationTimeout);
        validationTimeout = setTimeout(() => {
            // Additional validation logic if needed
        }, 300);
    }

    // Prevent form submission on invalid input
    guessForm.addEventListener('submit', function(e) {
        const value = guessInput.value.trim();
        if (!value || isNaN(parseInt(value))) {
            e.preventDefault();
            showError('Veuillez entrer un nombre valide');
            return false;
        }
    });

    // Add loading state cleanup
    window.addEventListener('beforeunload', function() {
        submitBtn.classList.remove('loading');
        submitBtn.disabled = false;
    });
});