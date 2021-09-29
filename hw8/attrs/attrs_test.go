package attrs

import (
    "testing"
    "math"
    "reflect"
)

var attrs = []Attr{{"a", 3}, {"b", 4}}

func TestHasAttr(t *testing.T) {
    want := true
    got := HasAttr(attrs, "b")
    if got != want {
        t.Fatalf(`HasAttr(attrs, "b") = %v, want %v`, got, want)
    }
}

func TestRemoveAttr(t *testing.T) {
    want := []Attr{{"b", 4}}
    got := RemoveAttr(attrs, "a")
    if !reflect.DeepEqual(got, want) {
        t.Fatalf(`TestRemove(attrs, "a") = %v, want %v`, got, want)
    }
}

func TestNonAttrVal(t *testing.T) {
    want := math.MinInt32
    got := NonAttrVal
    if got != want {
        t.Fatalf(`TestNonAttrVal = %v, want %v`, got, want)
    }
}

func TestUpdateAttr(t *testing.T) {
    want := []Attr{{"a", 17}, {"b", 4}}
    got := UpdateAttr(attrs, Attr{"a", 17})
    if !reflect.DeepEqual(got, want) {
        t.Fatalf(`TestUpdateAttr(attrs, Attr{"a", 17}) = %v, want %v`, got, want)
    }
    want = []Attr{{"b", 4}}
    got = UpdateAttr(attrs, Attr{"a", NonAttrVal})
    if !reflect.DeepEqual(got, want) {
        t.Fatalf(`TestUpdateAttr(attrs, Attr{"a", NonAttrVal}) = %v, want %v`, got, want)
    }
}

func TestUpdateMultiAttr(t *testing.T) {
    want := []Attr{{"b", 5}}
    got := UpdateMultiAttr(attrs, []Attr{{"b", 5}, {"a", NonAttrVal}})
    if !reflect.DeepEqual(got, want) {
        t.Fatalf(`TestUpdateMultiAttr(attrs, "a") = %v, want %v`, got, want)
    }
}

func TestAttrsFromString(t *testing.T) {
    want := []Attr{{"d", 3}, {"e", 4}}
    got := AttrsFromString("d 3 e 4")
    if !reflect.DeepEqual(got, want) {
        t.Fatalf(`TestAttrsFromString("d 3 e 4") = %v, want %v`, got, want)
    }
}
