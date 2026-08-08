/**
 * main.js — Global JavaScript utilities
 * =======================================
 * WHY THIS FILE EXISTS:
 *   Contains shared front-end logic used across multiple pages:
 *   auto-dismiss flash messages, smooth scroll, etc.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Auto-dismiss flash alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach((alert) => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});
