# Kowboy handbook - forms

Version 2026-11-06. How a form people fill in is built and measured, on any repository.
`HANDBOOK.md` says when to read this guide.

Goal: as many visitors as possible finish the form, and the receiver still gets what it needs to
act.

Figures are directional. They come from one benchmark article (Digital Applied, April 2026) that
shows no samples or method. Use them to choose what to try, never quote them to customers, and do
not add lifts together: combined effect is about 60-70 % of the sum. Our own measurements win.

- **Bot protection:** Every public-facing form has bot protection of some form.
- **Fields:** Every visible field must justify itself. Remove it, infer it from what is already
  known, or ask after submit. Conversion falls sharply past 5 fields, from 4 on phones (17.0 % at
  5, 11.4 % at 7).
- **Layout:** One column, easy fields first, sensitive or qualifying fields last. On 7+ fields,
  group fields into sections (+4-8 %) and hide irrelevant ones with conditional logic (+8-14 %).
- **Steps:** Split forms of 5+ fields into 2-3 steps with a progress indicator (+14 %, B2B +21 %).
  Keep forms of 3 or fewer fields on one step (-3 % if split). Four or more steps add little.
- **Validation:** Check each field when the visitor leaves it (+5 % on short forms, +11-13 % at 6+
  fields). Never hold errors until submit.
- **Autofill:** Set correct `autocomplete` and input `type` on every field (+11-18 % on mobile).
  Prefill what can be known, such as company from the e-mail domain (+9 %) and country (+4 %).
- **Button:** The label names the outcome, not "Submit" (+3-5 %).
- **Trust:** Put a visible privacy line by the button (+4-7 %); trust worries cause 19 % of
  abandonment. Put a customer quote next to demo and quote forms (+6-9 %).
- **High-commitment forms:** Demo and quote forms convert lowest (4.6 %, 9.8 %), so offer a
  lower-commitment option beside them.
- **Checkout and signup:** Show all costs early, never force account creation, offer express
  wallets on mobile (+22-34 %) and passkeys for signup (+9-14 %).
- **Measure:** Conversion is completions divided by people who interacted with the form, not page
  visitors. Track each form separately, and compare only within the same form type, field count,
  source and device. Phone lead forms converting about 32 % below desktop is normal.

End of the guide.
