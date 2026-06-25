# Defect Log — Saucedemo.com

## DEF_001
**Title:** Wrong product images displayed for problem_user  
**Severity:** High  
**Priority:** P1  
**Steps to Reproduce:**
1. Go to https://www.saucedemo.com
2. Log in with username: problem_user / password: secret_sauce
3. View the inventory page

**Expected Result:** Each product displays its correct image  
**Actual Result:** Product images are mismatched — wrong images shown for all products  
**Environment:** Chrome, saucedemo.com, macOS  
**Status:** Open  

---

## DEF_002
**Title:** Performance glitch causes 6+ second load time for performance_glitch_user  
**Severity:** High  
**Priority:** P2  
**Steps to Reproduce:**
1. Go to https://www.saucedemo.com
2. Log in with username: performance_glitch_user / password: secret_sauce
3. Observe login response time

**Expected Result:** Login completes within 2 seconds  
**Actual Result:** Login takes 6+ seconds — confirmed in automated test report  
**Environment:** Chrome, saucedemo.com, macOS  
**Status:** Open  

---

## DEF_003
**Title** "Remove" button displayed of "Add to Cart" for  Sauce Labs Backpack inventory page
**Severity:** High  
**Priority:** P2
**Steps to Reproduce:**
1. Go to https://www.saucedemo.com
2. Log in with username: problem_user / password: secret_sauce
3. View the inventory page

**Expected Result:** Each product displays Add to cart icon  
**Actual Result:** Add to cart are mismatched — Remove icon is shown for Sauce Labs Backpack product  
**Environment:** Chrome, saucedemo.com, macOS  
**Status:** Open  
