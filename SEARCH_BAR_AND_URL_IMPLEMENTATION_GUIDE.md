# Search Bar & URL Structure Implementation Guide

**Version:** 1.0  
**Last Updated:** February 10, 2026  
**Status:** Planning Document - For Future Implementation  
**Purpose:** Comprehensive guide for implementing search functionality and URL structure across all pages

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [URL Structure Planning](#url-structure-planning)
3. [Search Bar Implementation](#search-bar-implementation)
4. [Page Linking Strategy](#page-linking-strategy)
5. [SEO Considerations](#seo-considerations)
6. [Technical Requirements](#technical-requirements)
7. [Implementation Roadmap](#implementation-roadmap)

---

## Overview

This document outlines the strategy for implementing:

1. **Search Functionality** - Site-wide search bar with autocomplete
2. **URL Structure** - Clean, SEO-friendly URLs for all pages
3. **Internal Linking** - Consistent navigation and page connections
4. **User Experience** - Intuitive navigation and search features

### Goals

- Improve site navigation and discoverability
- Implement clean, semantic URLs
- Add powerful search functionality
- Enhance SEO performance
- Maintain consistency across all pages

---

## URL Structure Planning

### Current URL Structure

**Homepage:**
- Current: `/` or `/homepage-v1.html`
- Proposed: `/` (root)

**Product Categories:**
- Current: Various structures
- Proposed: Clean, hierarchical URLs

### Proposed URL Hierarchy

#### Main Categories

```
/fenster                    # Windows (main category)
/balkonturen               # Balcony doors
/rolladen                  # Shutters
/turen                     # Doors
/konfigurator              # Configurator tool
```

#### Product Subcategories

```
# Fenster (Windows) Subcategories
/fenster/kunststoff              # Plastic windows
/fenster/holz                    # Wood windows
/fenster/aluminium               # Aluminum windows
/fenster/holz-aluminium          # Wood-aluminum windows

# Fenster Manufacturers
/fenster/drutex                  # Drutex windows
/fenster/gealan                  # Gealan windows
/fenster/aluplast                # Aluplast windows
/fenster/salamander              # Salamander windows
/fenster/veka                    # Veka windows
/fenster/schueco                 # Schüco windows

# Balkontüren (Balcony Doors) Subcategories
/balkonturen/kunststoff          # Plastic balcony doors
/balkonturen/aluminium           # Aluminum balcony doors
/balkonturen/holz-aluminium      # Wood-aluminum balcony doors

# Rolläden (Shutters) Types
/rolladen/vorbau                 # Surface-mounted shutters
/rolladen/aufsatz                # Top-mounted shutters
/rolladen/unterputz              # Recessed shutters
```

#### Configurator Pages

```
/konfigurator/fenster            # Window configurator
/konfigurator/balkonturen        # Balcony door configurator
/konfigurator/rolladen           # Shutter configurator
```

#### Information Pages

```
/uber-uns                        # About us
/kontakt                         # Contact
/service                         # Service
/montage                         # Installation
/lieferung                       # Delivery
/zahlung                         # Payment
```

### URL Best Practices

**DO:**
- Use lowercase letters
- Use hyphens (-) for word separation
- Keep URLs short and descriptive
- Use German terms (primary language)
- Create logical hierarchy
- Make URLs human-readable

**DON'T:**
- Use underscores (_)
- Include file extensions (.html, .php)
- Use special characters (ä, ö, ü - use ae, oe, ue)
- Create deep nesting (max 3 levels)
- Use session IDs or tracking parameters
- Change URLs frequently (use redirects)

---

## Search Bar Implementation

### Search Bar Location

**Primary Location:** Header (sticky, always visible)

```html
<div class="search-bar-container">
    <form action="/suche" method="GET" class="search-form">
        <input type="search" 
               name="q" 
               placeholder="Fenster, Türen, Rolläden suchen..." 
               class="search-input"
               autocomplete="off"
               aria-label="Suchbegriff eingeben">
        <button type="submit" class="search-button" aria-label="Suchen">
            <i class="search-icon"></i>
        </button>
    </form>
    <div class="search-autocomplete" id="search-suggestions"></div>
</div>
```

### Search Features

#### Basic Search
- Full-text search across products
- Search in titles, descriptions, categories
- Highlight search terms in results

#### Advanced Search (Future)
- Filter by category (Fenster, Türen, etc.)
- Filter by manufacturer
- Filter by price range
- Filter by material
- Sort by relevance, price, popularity

#### Autocomplete/Suggestions

**Data Sources:**
1. Product names
2. Category names
3. Manufacturer names
4. Popular searches
5. Recent searches (user-specific)

**Implementation:**
```javascript
// Autocomplete example structure
const searchSuggestions = {
    products: [
        "Kunststofffenster",
        "Holzfenster",
        "Balkontür"
    ],
    manufacturers: [
        "Drutex",
        "Gealan",
        "Aluplast"
    ],
    categories: [
        "Fenster",
        "Rolläden",
        "Türen"
    ]
};
```

### Search Results Page

**URL:** `/suche?q=kunststofffenster`

**Content:**
```html
<div class="search-results">
    <h1>Suchergebnisse für "kunststofffenster"</h1>
    <div class="results-count">15 Ergebnisse gefunden</div>
    
    <div class="results-filters">
        <!-- Category filters -->
        <!-- Price range -->
        <!-- Manufacturer filters -->
    </div>
    
    <div class="results-list">
        <!-- Product cards -->
        <!-- Pagination -->
    </div>
</div>
```

---

## Page Linking Strategy

### Internal Link Structure

#### Navigation Menu (Global)

**Main Navigation:**
```html
<nav class="main-navigation">
    <a href="/fenster">Fenster</a>
    <a href="/balkonturen">Balkontüren</a>
    <a href="/rolladen">Rolläden</a>
    <a href="/konfigurator">Konfigurator</a>
</nav>
```

**Mega Menu (Dropdowns):**
```html
<div class="mega-menu fenster-menu">
    <div class="menu-column">
        <h3>Fenster nach Material</h3>
        <a href="/fenster/kunststoff">Kunststofffenster</a>
        <a href="/fenster/holz">Holzfenster</a>
        <a href="/fenster/aluminium">Aluminiumfenster</a>
    </div>
    <div class="menu-column">
        <h3>Hersteller</h3>
        <a href="/fenster/drutex">Drutex</a>
        <a href="/fenster/gealan">Gealan</a>
        <a href="/fenster/aluplast">Aluplast</a>
    </div>
</div>
```

#### Breadcrumb Navigation

**Structure:**
```html
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li><a href="/">Home</a></li>
        <li><a href="/fenster">Fenster</a></li>
        <li><a href="/fenster/kunststoff">Kunststofffenster</a></li>
        <li class="active">Drutex Kunststofffenster</li>
    </ol>
</nav>
```

**Benefits:**
- Improved user orientation
- Better SEO (structured data)
- Easy navigation back to parent pages

#### Footer Links

**Structure:**
```html
<footer class="site-footer">
    <div class="footer-column">
        <h4>Produkte</h4>
        <a href="/fenster">Fenster</a>
        <a href="/balkonturen">Balkontüren</a>
        <a href="/rolladen">Rolläden</a>
    </div>
    <div class="footer-column">
        <h4>Service</h4>
        <a href="/montage">Montage</a>
        <a href="/lieferung">Lieferung</a>
        <a href="/zahlung">Zahlung</a>
    </div>
    <div class="footer-column">
        <h4>Unternehmen</h4>
        <a href="/uber-uns">Über uns</a>
        <a href="/kontakt">Kontakt</a>
    </div>
</footer>
```

#### Related Products/Cross-Selling

**Example:**
```html
<section class="related-products">
    <h2>Passende Produkte</h2>
    <div class="product-grid">
        <a href="/fenster/drutex/iglo-5" class="product-card">...</a>
        <a href="/fenster/drutex/iglo-energy" class="product-card">...</a>
    </div>
</section>
```

---

## SEO Considerations

### URL Optimization

**SEO-Friendly URLs:**
- Descriptive and readable
- Include target keywords
- Use hyphens for separation
- Keep length under 60 characters
- Avoid unnecessary parameters

**Example:**
```
Good: /fenster/kunststoff/drutex-iglo-5
Bad:  /product.php?id=123&cat=windows&man=drutex
```

### Canonical URLs

**Purpose:** Avoid duplicate content issues

```html
<link rel="canonical" href="https://fenturo.com/fenster/kunststoff">
```

**Use Cases:**
- Product pages accessible via multiple URLs
- Pagination (all pages point to page 1)
- Filtered/sorted product listings

### Meta Tags

**Title Tags:**
```html
<title>Kunststofffenster von Drutex | FenTuRo</title>
```

**Meta Descriptions:**
```html
<meta name="description" content="Hochwertige Kunststofffenster von Drutex. Energieeffizient, langlebig und in vielen Designs erhältlich. Jetzt online konfigurieren!">
```

**Open Graph (Social Sharing):**
```html
<meta property="og:title" content="Kunststofffenster von Drutex">
<meta property="og:description" content="Hochwertige Fenster für Ihr Zuhause">
<meta property="og:image" content="/img/products/drutex-fenster.jpg">
<meta property="og:url" content="https://fenturo.com/fenster/kunststoff/drutex">
```

### Structured Data (Schema.org)

**Product Schema:**
```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Drutex Iglo 5 Kunststofffenster",
  "image": "/img/products/drutex-iglo-5.jpg",
  "description": "Energieeffizientes Kunststofffenster",
  "brand": {
    "@type": "Brand",
    "name": "Drutex"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://fenturo.com/fenster/kunststoff/drutex-iglo-5",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock"
  }
}
```

---

## Technical Requirements

### Frontend Requirements

#### HTML Structure
- Semantic HTML5 elements
- Accessible forms (ARIA labels)
- Proper heading hierarchy (h1, h2, h3)
- Valid markup (W3C validation)

#### CSS/Styling
- Responsive design (mobile-first)
- Consistent styling across pages
- Loading states for search
- Hover/focus states for links

#### JavaScript
- Progressive enhancement (works without JS)
- Autocomplete functionality
- Form validation
- Analytics tracking

### Backend Requirements

#### Server Configuration
- URL rewriting (Apache mod_rewrite or Nginx)
- 301 redirects for old URLs
- Custom 404 error pages
- Proper caching headers

#### Search Implementation
- Full-text search engine (Elasticsearch, Algolia, or similar)
- Search index of all products
- Fast response times (<100ms)
- Relevance ranking

#### Data Requirements
- Product database with searchable fields
- Category/taxonomy structure
- Manufacturer information
- Product images and descriptions

---

## Implementation Roadmap

### Phase 1: URL Structure (Weeks 1-2)

**Tasks:**
1. Define complete URL hierarchy
2. Set up URL rewriting rules
3. Implement 301 redirects from old URLs
4. Update all internal links
5. Test all URLs

**Deliverables:**
- URL mapping document
- Server configuration files
- Redirect rules file
- Updated navigation menu

### Phase 2: Search Bar UI (Weeks 3-4)

**Tasks:**
1. Design search bar component
2. Implement HTML/CSS
3. Add to header (sticky position)
4. Make responsive
5. Test accessibility

**Deliverables:**
- Search bar component
- CSS styling
- Responsive behavior
- Accessibility compliance

### Phase 3: Search Functionality (Weeks 5-6)

**Tasks:**
1. Set up search backend
2. Index all products
3. Implement search API
4. Build results page
5. Add filters and sorting

**Deliverables:**
- Search API endpoint
- Product index
- Results page template
- Filter components

### Phase 4: Autocomplete (Weeks 7-8)

**Tasks:**
1. Build suggestion database
2. Implement autocomplete API
3. Add frontend autocomplete
4. Handle keyboard navigation
5. Optimize performance

**Deliverables:**
- Autocomplete component
- Suggestion API
- Keyboard navigation
- Performance optimization

### Phase 5: Testing & Optimization (Weeks 9-10)

**Tasks:**
1. Cross-browser testing
2. Mobile device testing
3. Performance optimization
4. SEO verification
5. User testing

**Deliverables:**
- Test reports
- Bug fixes
- Performance improvements
- SEO audit results

---

## Code Examples

### URL Rewriting (Apache .htaccess)

```apache
# Enable URL rewriting
RewriteEngine On

# Remove .html extension
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}\.html -f
RewriteRule ^(.*)$ $1.html [L]

# Fenster category
RewriteRule ^fenster$ /fenster.html [L]
RewriteRule ^fenster/([a-z-]+)$ /fenster-$1.html [L]

# Search page
RewriteRule ^suche$ /search.html [QSA,L]

# 301 Redirects for old URLs
Redirect 301 /old-fenster.html /fenster
Redirect 301 /products/windows /fenster
```

### Search Form Component

```html
<div class="search-wrapper" data-component="search">
    <form action="/suche" method="GET" role="search" class="search-form">
        <div class="search-input-group">
            <label for="search-input" class="sr-only">Suchbegriff</label>
            <input type="search" 
                   id="search-input"
                   name="q" 
                   class="search-input"
                   placeholder="Produkte suchen..."
                   autocomplete="off"
                   aria-autocomplete="list"
                   aria-controls="search-suggestions"
                   aria-expanded="false">
            
            <button type="submit" 
                    class="search-submit"
                    aria-label="Suchen">
                <svg class="search-icon" width="20" height="20">
                    <use href="#icon-search"></use>
                </svg>
            </button>
        </div>
        
        <div id="search-suggestions" 
             class="search-suggestions"
             role="listbox"
             hidden>
            <!-- Autocomplete results inserted here -->
        </div>
    </form>
</div>
```

### Search JavaScript (Basic)

```javascript
class SearchComponent {
    constructor(element) {
        this.element = element;
        this.input = element.querySelector('.search-input');
        this.suggestions = element.querySelector('.search-suggestions');
        this.debounceTimer = null;
        
        this.init();
    }
    
    init() {
        this.input.addEventListener('input', (e) => this.handleInput(e));
        this.input.addEventListener('focus', () => this.showSuggestions());
        this.input.addEventListener('blur', () => this.hideSuggestions());
    }
    
    handleInput(e) {
        clearTimeout(this.debounceTimer);
        
        const query = e.target.value.trim();
        
        if (query.length < 2) {
            this.hideSuggestions();
            return;
        }
        
        this.debounceTimer = setTimeout(() => {
            this.fetchSuggestions(query);
        }, 300);
    }
    
    async fetchSuggestions(query) {
        try {
            const response = await fetch(`/api/search/suggest?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            this.renderSuggestions(data.suggestions);
        } catch (error) {
            console.error('Search suggestions error:', error);
        }
    }
    
    renderSuggestions(suggestions) {
        if (!suggestions || suggestions.length === 0) {
            this.hideSuggestions();
            return;
        }
        
        const html = suggestions.map(item => `
            <a href="${item.url}" class="suggestion-item" role="option">
                <span class="suggestion-text">${item.title}</span>
                <span class="suggestion-category">${item.category}</span>
            </a>
        `).join('');
        
        this.suggestions.innerHTML = html;
        this.suggestions.hidden = false;
        this.input.setAttribute('aria-expanded', 'true');
    }
    
    showSuggestions() {
        if (this.suggestions.innerHTML) {
            this.suggestions.hidden = false;
            this.input.setAttribute('aria-expanded', 'true');
        }
    }
    
    hideSuggestions() {
        setTimeout(() => {
            this.suggestions.hidden = true;
            this.input.setAttribute('aria-expanded', 'false');
        }, 200);
    }
}

// Initialize search component
document.addEventListener('DOMContentLoaded', () => {
    const searchElement = document.querySelector('[data-component="search"]');
    if (searchElement) {
        new SearchComponent(searchElement);
    }
});
```

---

## Testing Checklist

### URL Structure Testing

- [ ] All main category URLs work
- [ ] All subcategory URLs work
- [ ] All product URLs work
- [ ] Old URLs redirect correctly (301)
- [ ] No broken links in navigation
- [ ] Breadcrumbs generate correctly
- [ ] URLs are SEO-friendly

### Search Functionality Testing

- [ ] Search form submits correctly
- [ ] Search results display properly
- [ ] Filters work as expected
- [ ] Sorting works correctly
- [ ] Pagination functions
- [ ] No results message displays
- [ ] Search highlights work

### Autocomplete Testing

- [ ] Suggestions appear after 2 characters
- [ ] Suggestions are relevant
- [ ] Keyboard navigation works (arrow keys)
- [ ] Click on suggestion navigates
- [ ] Suggestions hide when appropriate
- [ ] No performance issues
- [ ] Mobile touch events work

### Accessibility Testing

- [ ] Screen reader compatibility
- [ ] Keyboard navigation complete
- [ ] ARIA labels present
- [ ] Focus states visible
- [ ] Color contrast sufficient
- [ ] Forms are labeled

### Performance Testing

- [ ] Page load time < 3 seconds
- [ ] Search response < 1 second
- [ ] Autocomplete response < 300ms
- [ ] Images optimized
- [ ] CSS/JS minified
- [ ] Caching implemented

---

## Best Practices Summary

### URLs
✅ Use clean, descriptive URLs  
✅ Implement breadcrumbs  
✅ Set up 301 redirects  
✅ Use canonical tags  
✅ Keep URLs short and simple  

### Search
✅ Place search prominently  
✅ Implement autocomplete  
✅ Show result count  
✅ Provide filters  
✅ Highlight search terms  

### Links
✅ Use descriptive anchor text  
✅ Ensure all links work  
✅ Add hover/focus states  
✅ Implement breadcrumbs  
✅ Test internal linking  

### SEO
✅ Optimize meta tags  
✅ Use structured data  
✅ Create XML sitemap  
✅ Implement canonical URLs  
✅ Monitor search performance  

---

## Resources & Tools

### Development Tools
- [ModRewrite Tester](https://htaccess.madewithlove.be/) - Test Apache rewrite rules
- [Regex101](https://regex101.com/) - Test regular expressions
- [PageSpeed Insights](https://pagespeed.web.dev/) - Performance testing

### SEO Tools
- [Google Search Console](https://search.google.com/search-console)
- [Screaming Frog SEO Spider](https://www.screamingfrog.co.uk/seo-spider/)
- [Ahrefs](https://ahrefs.com/) - Backlink analysis
- [SEMrush](https://www.semrush.com/) - Keyword research

### Accessibility Tools
- [WAVE](https://wave.webaim.org/) - Accessibility checker
- [axe DevTools](https://www.deque.com/axe/devtools/) - Browser extension
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Audit tool

---

## Version History

### Version 1.0 (February 10, 2026)
- Initial planning document
- URL structure defined
- Search functionality outlined
- Implementation roadmap created

---

## Next Steps

1. **Review & Approve** - Review this document with stakeholders
2. **Prioritize** - Decide which features to implement first
3. **Design** - Create mockups for search UI
4. **Develop** - Begin Phase 1 implementation
5. **Test** - Comprehensive testing at each phase
6. **Deploy** - Staged rollout to production

---

**End of Search Bar & URL Implementation Guide**

**Status:** Ready for implementation planning  
**Contact:** Development team for questions and clarifications
