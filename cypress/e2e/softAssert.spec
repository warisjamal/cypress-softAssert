describe("Scenario-1 with native assertions", () => {
    it('should validate multiple assertions using native assertions', () => {
        cy.visit('https://www.saucedemo.com/');
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();
        cy.get('#react-burger-menu-btn').click();
        cy.get('a#inventory_sidebar_link').should('have.text', 'All Item');
        cy.get('button#react-burger-cross-btn').click();

        cy.get('button#add-to-cart-sauce-labs-backpack').should('have.text', 'Add to cart');
        cy.get('.app_logo').should('contain', 'Swag Labs');
        cy.get('div#inventory_container').last().should('have.class', 'inventory_container');
        cy.get('.inventory_item').should('have.length', 6);
        cy.get('img[alt="Sauce Labs Backpack"]').should('have.attr', 'src', '/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg');
    });
});
describe("Scenario-2 with SoftAssertions", () => {
    after("This will store all the errors for all the describe blocks", function () {
        cy.assertAll(); // This we need to add for throwing the errors
    });

    it('should validate multiple assertions using softAssert', () => {
        cy.visit('https://www.saucedemo.com/');
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();
        cy.get('#react-burger-menu-btn').click();
        cy.get('a#inventory_sidebar_link').then($el => {
            cy.softAssert($el.text(), 'All Item', 'The text should be "All Items"');
        });
        cy.get('a#inventory_sidebar_link').then($el => {
            cy.softAssert($el.text(), 'All Item', 'The text should be "All Items"');
        });
        cy.get('button#react-burger-cross-btn').click();
        cy.get('button#add-to-cart-sauce-labs-backpack').then($el => {
            cy.softAssert($el.text(), 'Add to cart', 'The text should be "Add to cart"');
        });
        // should('contain')
        cy.get('.app_logo').then($el => {
            cy.softAssert($el.text().includes('Swasg Labs'), true, 'The element should contain Swag Labs');
        });
        // should('have.class')
        cy.get('div#inventory_container').then($el => {
            cy.softAssert($el.hasClass('inventory_containesr'), true, 'The element should have the class "inventory_container"');
        });
        // should('not.have.class')
        cy.get('div#inventory_container').then($el => {
            cy.softAssert(!$el.hasClass('inventorsy'), true, 'The element should not have the class "inventory"');
        });
        cy.get('.inventory_item').then($el => {
            cy.softAssert($el.length, 4, 'The length should be 6');
        })
        cy.get('img[alt="Sauce Labs Backpack"]').then($el => {
            cy.softAssert($el.attr('src'), '/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg', 'attribute should be present');
        });
    });
});
