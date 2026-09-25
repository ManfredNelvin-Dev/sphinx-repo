#!/bin/bash

export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

VERSIONS=("16.0" "17.0" "18.0" "19.0" "main")
LANGS=("en" "nl" "de" "fr")

rm -rf build/site

for VERSION in "${VERSIONS[@]}"
do
    echo "Building version $VERSION"

    git checkout "$VERSION"

    for LANG in "${LANGS[@]}"
    do
        echo "  Building language $LANG"

        sphinx-build \
            -D language="$LANG" \
            -b html \
            source \
            "build/site/$VERSION/$LANG"
    done
done

git checkout main