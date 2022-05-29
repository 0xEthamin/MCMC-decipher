from library import *

# Put your ciphered text here
ciphered_text = """qxup nycp pxnds qyu ad kd zryup vxp jc ut h xue md wykkd yc md qxcnxupd puecxeuyk qyu pu ad mdnxup rdpcqdr qx nud xcaycrm fcu xndz nycp ad murxup jcd z dpe m xwyrm mdp rdkzykerdp mdp odkp jcu q yke edkmc tx qxuk vdce derd x ck qyqdke yc ad kd vycnxup vxp yc a dexup pdct zfds qyu de z dpe xppds zcrudcb md pd murd jcd tdp fxpxrmp tdp rdkzykerdp iyrodke ckd mdpeukdd vxrzd jcd jcxkm yk x td oyce md tx zfypd jcxkm yk x td oyce md tx zfypd wudk ixued td wdxc odped vxriyup yk kd erycnd vxp t ukedrtyzcedcr dk ixzd ad murxup td quryur jcu nycp xumd x xnxkzdr xtyrp zd k dpe vxp qyk zxp zyqqd ad td mupxup tx vcupjcd qyu xc zykerxurd a xu vc de ad mup qdrzu x tx nud ad tcu mup qdrzu ad zfxked tx nud ad mxkpd tx nud ad kd pcup jc xqycr de iukxtdqdke jcxkm wdxczycv md odkp xcaycrm fcu qd mupdke qxup zyqqdke ixup ec vycr xnyur zdeed fcqxkued df wudk ad tdcr rdvykmp erdp puqvtdqdke ad tdcr mup jcd z dpe zd oyce md t xqycr zd oyce mykz jcu q x vycppd xcaycrm fcu x dkerdvrdkmrd ckd zykperczeuyk qdzxkujcd qxup mdqxuk jcu pxue vdce derd puqvtdqdke x qd qdeerd xc pdrnuzd md tx zyqqckxced x ixurd td myk td myk md pyu"""

# The maximum number of tests that the program will do
MAX_TEST = 100000


# Calculation of the probabilities of bigrams of a language according to a text. Here it's "Du coté de chez swann" a french text.
probability_dictionary = bigrams_proba("proust.txt")


# Generation of a new deciphering alphabet
current_alphabet = get_new_random_alphabet()

current_deciphered_text = decipher(ciphered_text, current_alphabet)
current_score = score_calculator(current_deciphered_text, probability_dictionary)

# Initialization of the variables used for the print
best_deciphered_text = current_deciphered_text
best_score = current_score

for i in range(MAX_TEST):

    # Make a new attempt and calculate it's score
    attempt_alphabet = permute_alphabet(current_alphabet, random.randint(0, 25), random.randint(0, 25))  # Generation of a new deciphering alphabet with a random permutation
    attempt_deciphered_text = decipher(ciphered_text, attempt_alphabet)
    attempt_score = score_calculator(attempt_deciphered_text, probability_dictionary)

    ########################
    # METROPOLIS ALGORITHM #
    ########################

    ratio = np.exp((attempt_score - current_score) * len(ciphered_text))  # Calculates the ratio of the probability of the attempt to the old probability.
    random_number = random.uniform(0, 1)  # Generate a random number between 0 and 1

    if random_number < ratio:
        current_alphabet = attempt_alphabet.copy()
        current_deciphered_text = attempt_deciphered_text
        current_score = attempt_score

        #################
        # PRINT GESTION #
        #################

        if current_score > best_score:
            best_score = current_score
            best_deciphered_text = current_deciphered_text
            print(best_deciphered_text, " score = ", best_score)
