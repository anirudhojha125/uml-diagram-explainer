// DOM Elements
const diagramCards = document.querySelectorAll('.card[data-diagram]');
const teamCards = document.querySelectorAll('.card[data-member]');
const detailContents = document.querySelectorAll('.detail-content');
const memberDetails = document.querySelectorAll('#student-developer-detail, #student-developer-2-detail, #supervising-instructor-detail, #class-contributors-detail');
const ctaButton = document.querySelector('.cta-button');
const diagramsSection = document.getElementById('diagrams');
const navLinks = document.querySelectorAll('.nav-links a');
const darkModeToggle = document.getElementById('dark-mode-toggle');

// Show the first diagram by default
document.addEventListener('DOMContentLoaded', function() {
    // Show the use case diagram by default
    showDiagram('use-case');
    
    // Add event listeners to diagram cards
    diagramCards.forEach(card => {
        card.addEventListener('click', function() {
            const diagramType = this.getAttribute('data-diagram');
            showDiagram(diagramType);
            
            // Scroll to details section
            document.querySelector('.diagram-details').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'nearest'
            });
        });
    });
    
    // Add event listeners to team member cards
    teamCards.forEach(card => {
        card.addEventListener('click', function() {
            const memberType = this.getAttribute('data-member');
            showMemberDetail(memberType);
            
            // Scroll to details section
            document.querySelector('.member-details').scrollIntoView({ 
                behavior: 'smooth', 
                block: 'nearest'
            });
        });
    });
    
    // Add event listener to CTA button
    ctaButton.addEventListener('click', function() {
        diagramsSection.scrollIntoView({ behavior: 'smooth' });
    });
    
    // Add event listeners to navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({ 
                behavior: 'smooth' 
            });
        });
    });
    
    // Add event listener for dark mode toggle
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', toggleDarkMode);
        
        // Check for saved theme preference or respect OS preference
        const savedTheme = localStorage.getItem('theme');
        const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
        
        if (savedTheme === 'dark' || (!savedTheme && prefersDarkScheme.matches)) {
            document.body.classList.add('dark-mode');
            darkModeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        }
    }
});

// Function to show a specific diagram
function showDiagram(diagramType) {
    // Hide all detail contents
    detailContents.forEach(content => {
        content.classList.remove('active');
    });
    
    // Show the selected diagram
    const selectedDetail = document.getElementById(`${diagramType}-detail`);
    if (selectedDetail) {
        selectedDetail.classList.add('active');
        
        // Force image reload to ensure they display properly
        const images = selectedDetail.querySelectorAll('img');
        images.forEach(img => {
            // Store the original source
            const src = img.src;
            // Force reload by clearing and resetting the src
            img.src = '';
            setTimeout(() => {
                img.src = src;
            }, 10);
        });
    }
    
    // Update active card styling
    diagramCards.forEach(card => {
        if (card.getAttribute('data-diagram') === diagramType) {
            card.classList.add('active');
        } else {
            card.classList.remove('active');
        }
    });
    
    // Add animation effect
    animateDiagramChange();
}

// Function to show a specific team member detail
function showMemberDetail(memberType) {
    // Hide all member detail contents
    memberDetails.forEach(content => {
        content.classList.remove('active');
    });
    
    // Show the member details section
    document.querySelector('.member-details').style.display = 'block';
    
    // Show the selected member detail
    const selectedDetail = document.getElementById(`${memberType}-detail`);
    if (selectedDetail) {
        selectedDetail.classList.add('active');
    }
    
    // Update active card styling
    teamCards.forEach(card => {
        if (card.getAttribute('data-member') === memberType) {
            card.classList.add('active');
        } else {
            card.classList.remove('active');
        }
    });
    
    // Add animation effect
    animateMemberChange();
}

// Function to add animation effect when changing diagrams
function animateDiagramChange() {
    const detailContainer = document.querySelector('.diagram-details');
    detailContainer.style.opacity = '0';
    
    setTimeout(() => {
        detailContainer.style.transition = 'opacity 0.3s ease';
        detailContainer.style.opacity = '1';
    }, 10);
}

// Function to add animation effect when changing member details
function animateMemberChange() {
    const detailContainer = document.querySelector('.member-details');
    detailContainer.style.opacity = '0';
    
    setTimeout(() => {
        detailContainer.style.transition = 'opacity 0.3s ease';
        detailContainer.style.opacity = '1';
    }, 10);
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70,
                behavior: 'smooth'
            });
        }
    });
});

// Add animation to cards on scroll
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animated');
        }
    });
}, observerOptions);

document.querySelectorAll('.card').forEach(card => {
    observer.observe(card);
});

// Add header shadow on scroll
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.style.boxShadow = '0 4px 10px rgba(0,0,0,0.1)';
        header.style.background = 'rgba(44, 62, 80, 0.95)';
    } else {
        header.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
        header.style.background = '#2c3e50';
    }
});

// Add hover effect to images
document.querySelectorAll('.detail-content img').forEach(img => {
    img.addEventListener('mouseover', function() {
        this.style.transform = 'scale(1.02)';
    });
    
    img.addEventListener('mouseout', function() {
        this.style.transform = 'scale(1)';
    });
    
    // Add error handling for images
    img.addEventListener('error', function() {
        console.log('Image failed to load, showing fallback...');
        // The onerror attribute in HTML will handle the fallback
    });
});

// Dark mode toggle function
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    
    // Update button icon
    const isDarkMode = document.body.classList.contains('dark-mode');
    darkModeToggle.innerHTML = isDarkMode ? 
        '<i class="fas fa-sun"></i>' : 
        '<i class="fas fa-moon"></i>';
    
    // Save preference to localStorage
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
}