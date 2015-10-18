ENTITY equiv IS
    PORT (a, b : IN BIT;
          c    : OUT BIT);
END equiv;

ARCHITECTURE structure OF equiv IS

    SIGNAL tmp : BIT;

    COMPONENT xor2
        PORT (x, y : IN BIT; z : OUT BIT);
    END COMPONENT;

    COMPONENT inv
        PORT (x : IN BIT; z : OUT BIT);
    END COMPONENT;

BEGIN

    u0: xor2 PORT MAP (a, b, tmp);
    u1: inv PORT MAP (tmp, c);

END structure;
