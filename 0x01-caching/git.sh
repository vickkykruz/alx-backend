git add $1
concatenated=""
for args in "${@:2}"; do
  concatenated="$concatenated $args"
done
git commit -m "$concatenated"
git push
