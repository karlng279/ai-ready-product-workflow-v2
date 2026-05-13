---
artifact: NSM
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: pm-data-analytics
upstream: market-research.md
downstream: growth.md
---

# Export Customs Clearances Data Analytics

**Product / Team:** Export Customs Clearances  
**Date:** 2026-05-13  
**Owner:** Product Team  
**Measurement Stage:** Pre-instrumentation draft

---

## Analytics Context

This artifact defines the measurement system before production data is collected. Baselines are marked `TBD` where instrumentation or historical reporting is not yet available. The first analytics milestone is to instrument booking-time VAS exposure, selection, support start, support completion, customer feedback, and operational exceptions.

---

## North Star Metric

### What is Our North Star Metric?

The North Star Metric is the single number that best captures customer value delivered by Export Customs Clearances. For this product, value is not just that customers buy the VAS; value is delivered when clearance support starts early enough to reduce uncertainty before shipment deadlines.

### North Star Metric Definition

| Attribute | Value |
|-----------|-------|
| **NSM Name** | Weekly Clearance-Supported Export Bookings |
| **NSM Definition** | Count of eligible export bookings per week where the customer selected Export Customs Clearances and the first carrier-side support action occurred within 24 hours of booking confirmation. |
| **Current Value** | 0 |
| **Target (12 months)** | TBD after pilot; initial planning target: 15% of eligible export bookings with timely support action |
| **Measurement frequency** | Weekly |
| **Data source** | Booking events, VAS selection events, support case events, operations SLA tracking |

**Why this is our NSM:**  
This metric captures customer value because it counts bookings where the customer both requested help and received timely support. It is a leading indicator for VAS revenue, repeat adoption, customer confidence, and lower clearance-related escalation.

**Counter-metrics (protect against gaming):**
- Booking abandonment rate must not increase by more than 2 percentage points after VAS offer exposure.
- Customer satisfaction for purchased/requested support must stay at or above 4.2/5.
- Clearance-support SLA breach rate must stay below 15%.
- Refund, complaint, or liability escalation rate must stay below an agreed compliance threshold.

---

## Input Metrics

| Input Metric | Definition | Current | Target | Owner Team |
|--------------|------------|---------|--------|------------|
| Eligible offer exposure rate | Eligible export bookings where the VAS offer is displayed / all eligible export bookings | TBD | 95% | Product / Engineering |
| VAS selection rate | Bookings with Export Customs Clearances selected / bookings exposed to the offer | 0% | 8% by 2026-08-31 | Product / Commercial |
| First support action within 24h | Selected VAS bookings with first carrier-side support action within 24h / selected VAS bookings | 0% | 85% by 2026-08-31 | Operations |
| Scope clarity rate | Customers who answer "I understand what support includes" positively after selection / surveyed selected customers | TBD | 80% | Product / CX |
| Support completion rate | Selected VAS bookings with support completed or handed off before documentation cutoff / selected VAS bookings | TBD | 80% | Operations |
| Repeat selection rate | Customers who select Export Customs Clearances again within 90 days / customers who selected it once | TBD | 25% | Product / Commercial |

---

## NSM Decomposition Tree

```
North Star: Weekly Clearance-Supported Export Bookings
|
+-- Eligible offer exposure rate
|   +-- Sub-metric: Eligibility rules coverage
|   +-- Sub-metric: Offer render success rate
|
+-- VAS selection rate
|   +-- Sub-metric: Offer click-through rate
|   +-- Sub-metric: Offer selection completion rate
|   +-- Sub-metric: Price acceptance rate
|
+-- First support action within 24h
|   +-- Sub-metric: Support case creation success rate
|   +-- Sub-metric: Operations assignment time
|   +-- Sub-metric: First customer contact time
|
+-- Support completion rate
|   +-- Sub-metric: Required information received rate
|   +-- Sub-metric: Pending customer action aging
|   +-- Sub-metric: Before-cutoff handoff completion
|
+-- Repeat selection rate
    +-- Sub-metric: Post-service satisfaction
    +-- Sub-metric: Repeat eligible booking volume
```

---

## HEART Metrics

| HEART Dimension | Metric | Signal | Data Source | Target |
|-----------------|--------|--------|-------------|--------|
| Happiness | Post-support CSAT | Customer feels helped and less uncertain | Post-service survey | 4.2/5 pilot, 4.4/5 at scale |
| Adoption | VAS selection rate | Customers discover and choose the booking-time offer | Booking analytics | 8% pilot, 15% 12-month |
| Retention | Repeat selection rate | Customers reuse the service for future eligible bookings | Booking/customer cohort analytics | 25% within 90 days |
| Task Success | First support action within 24h | Customer receives timely support after selecting the service | Support workflow events | 85% pilot, 90% 12-month |
| Task Success | Support completed before cutoff | Support reaches completion or proper handoff before deadline | Support + shipment milestone events | 80% pilot |

---

## NSM Dashboard

| Metric | This Week | Last Week | 4-Week Trend | Target |
|--------|-----------|-----------|--------------|--------|
| **NSM: Weekly Clearance-Supported Export Bookings** | TBD | TBD | TBD | 15% of eligible bookings |
| Eligible offer exposure rate | TBD | TBD | TBD | 95% |
| VAS selection rate | TBD | TBD | TBD | 8% pilot |
| First support action within 24h | TBD | TBD | TBD | 85% pilot |
| Support completion rate | TBD | TBD | TBD | 80% pilot |
| Post-support CSAT | TBD | TBD | TBD | 4.2/5 pilot |
| Booking abandonment after offer exposure | TBD | TBD | TBD | No more than +2pp |

---

## Alerting Thresholds

| Metric | Green | Yellow (Monitor) | Red (Act Immediately) |
|--------|-------|------------------|-----------------------|
| Weekly Clearance-Supported Export Bookings | At or above weekly target | 80%-99% of weekly target | Below 80% of weekly target |
| VAS selection rate | >= 8% pilot | 5%-7.9% | < 5% |
| First support action within 24h | >= 85% | 70%-84.9% | < 70% |
| Support completion before cutoff | >= 80% | 65%-79.9% | < 65% |
| Post-support CSAT | >= 4.2/5 | 3.8-4.19/5 | < 3.8/5 |
| Booking abandonment after offer exposure | <= +1pp | +1pp to +2pp | > +2pp |

---

## Funnel Analysis

**Funnel Name:** Booking-Time Export Customs Clearance VAS Funnel  
**Date:** 2026-05-13  
**Owner:** Product Team  
**Time Period:** Pilot period, once launched

### Funnel Framework Selection

**Selected framework:** Custom funnel

**Rationale:** This is a booking-embedded VAS flow, not a standalone acquisition funnel. The critical journey is offer exposure -> selection -> timely support -> successful support outcome -> repeat selection.

### Funnel Definition

| Stage | Event Name | Definition | Metric | Current Rate |
|-------|------------|------------|--------|--------------|
| Eligible booking created | `export_booking_eligible_for_ecc` | Export booking meets lane, customer, and service eligibility rules | Eligible bookings | TBD |
| Offer exposed | `ecc_offer_viewed` | Customer sees Export Customs Clearances option during booking | Offer exposure rate | TBD |
| Offer details opened | `ecc_offer_details_opened` | Customer opens service details, tooltip, or modal | Detail engagement rate | TBD |
| Service selected | `ecc_service_selected` | Customer selects the VAS during booking | Selection rate | 0% |
| Booking completed with service | `booking_completed_with_ecc` | Booking is confirmed with VAS request/purchase attached | Selection completion rate | 0% |
| Support case created | `ecc_support_case_created` | Internal support workflow is created from booking | Case creation success rate | TBD |
| First support action | `ecc_first_support_action_completed` | Carrier-side support action occurs within 24h | SLA success rate | 0% |
| Support completed or handed off | `ecc_support_completed_or_handed_off` | Support reaches defined completion or proper handoff before cutoff | Support completion rate | TBD |
| Feedback submitted | `ecc_post_support_feedback_submitted` | Customer submits post-support survey | Feedback response rate | TBD |
| Repeat selection | `ecc_repeat_service_selected` | Same customer selects ECC on another eligible booking within 90 days | Repeat selection rate | TBD |

### Bottleneck Hypotheses

| Potential Bottleneck | Root Cause Hypothesis | Evidence Needed |
|----------------------|-----------------------|-----------------|
| Offer viewed -> Service selected | Customers do not understand scope or value quickly enough during booking. | Click-through, detail-open rate, selection rate, survey reason for non-selection |
| Service selected -> Booking completed | The service creates checkout friction or pricing anxiety. | Booking abandonment segmented by offer exposure and selection |
| Booking completed -> First support action | Operations workflow or handoff is not fast enough. | Support case timestamp, assignment timestamp, first-contact timestamp |
| First support action -> Satisfaction | Support action does not visibly reduce customer uncertainty. | CSAT, qualitative feedback, unresolved issue rate |

### Optimization Opportunities

| Stage | Problem | Proposed Fix | Expected Impact | Effort |
|-------|---------|--------------|-----------------|--------|
| Offer exposure | Generic offer may not feel relevant | Add lane/risk-specific recommendation copy | +10%-20% relative selection | M |
| Offer details | Scope ambiguity blocks trust | Add "Included / Not included / What happens next" details | +15% relative detail-to-selection conversion | S |
| Post-selection | No visible next step | Add support owner, SLA timestamp, and pending-action summary | +10pp support confidence | M |
| Operations handoff | Manual routing may breach SLA | Auto-create support case with required booking context | +15pp 24h SLA success | M |

---

## Event Instrumentation Plan

| Event Name | Trigger | Required Properties |
|------------|---------|---------------------|
| `export_booking_eligible_for_ecc` | Booking enters a flow where ECC eligibility rules evaluate true | `booking_id`, `customer_id`, `origin`, `destination`, `trade_lane`, `cargo_type`, `cutoff_datetime`, `eligibility_rule_id` |
| `ecc_offer_viewed` | ECC offer is rendered to customer | `booking_id`, `customer_id`, `placement`, `message_variant`, `price_shown`, `currency`, `eligible_reason` |
| `ecc_offer_details_opened` | Customer opens details, tooltip, or modal | `booking_id`, `customer_id`, `content_version`, `message_variant` |
| `ecc_service_selected` | Customer selects ECC option | `booking_id`, `customer_id`, `price`, `currency`, `message_variant`, `selection_type` |
| `ecc_service_deselected` | Customer removes ECC option before booking completion | `booking_id`, `customer_id`, `price`, `message_variant` |
| `booking_completed_with_ecc` | Booking is confirmed with ECC attached | `booking_id`, `customer_id`, `price`, `currency`, `payment_status`, `selected_at`, `booking_completed_at` |
| `ecc_support_case_created` | Support case is created from selected ECC booking | `booking_id`, `case_id`, `created_at`, `assigned_team`, `sla_due_at` |
| `ecc_first_support_action_completed` | First support action is logged | `booking_id`, `case_id`, `action_type`, `action_at`, `hours_since_booking`, `within_24h` |
| `ecc_customer_action_requested` | Customer is asked for missing information or documents | `booking_id`, `case_id`, `requested_item_type`, `owner`, `due_at` |
| `ecc_support_completed_or_handed_off` | Support is completed or formally handed off | `booking_id`, `case_id`, `completion_type`, `completed_at`, `before_cutoff`, `outcome_status` |
| `ecc_post_support_feedback_submitted` | Customer submits post-support survey | `booking_id`, `customer_id`, `csat_score`, `scope_clarity_score`, `free_text_present` |

---

## A/B Test Design

**Test Name:** ECC Offer Message - Risk Reduction vs. Convenience  
**Test Owner:** Product Team  
**Date:** 2026-05-13  
**Status:** Draft

### Background

**Problem / Opportunity:**  
Market research suggests customers may evaluate Export Customs Clearances based on risk reduction, scope clarity, and first-action confidence. We need to test whether delay-risk messaging produces stronger booking-time intent than convenience messaging.

**Hypothesis:**  
"We believe that risk-reduction messaging will increase `ecc_service_selected` rate for eligible export booking customers because clearance delay avoidance is more urgent than convenience. We'll know we're right if selection rate improves by at least 20% relative within a minimum 14-day test."

### Variants

| Variant | Description | Visual / Technical Change |
|---------|-------------|---------------------------|
| Control A | Convenience message | "Get extra support coordinating export clearance documents after booking." |
| Treatment B | Risk-reduction message | "Reduce export clearance delay risk with carrier-side support started after booking." |

### Audience

| Attribute | Value |
|-----------|-------|
| **Target segment** | Eligible export booking customers in pilot lanes |
| **Traffic split** | 50/50 |
| **Geographic scope** | Pilot lanes only |
| **Exclusions** | Internal/test accounts, customers with unavailable service lanes, bookings created by support agents on behalf of customers |

### Metrics

**Primary Metric**

| Metric | Current Value | Minimum Detectable Effect | Expected Lift |
|--------|---------------|---------------------------|---------------|
| `ecc_service_selected` / `ecc_offer_viewed` | TBD; planning assumption 8% | +20% relative | 8% -> 9.6% |

**Secondary Metrics**

| Metric | Direction | Notes |
|--------|-----------|-------|
| `ecc_offer_details_opened` rate | Increase | Indicates interest or need for clarity |
| `booking_completed_with_ecc` rate | Increase | Ensures selection survives booking completion |
| Scope clarity score | Increase | Validates message comprehension |

**Guard-rail Metrics**

| Metric | Threshold | Why |
|--------|-----------|-----|
| Booking abandonment after offer exposure | Must not increase by >2pp | Protect core booking conversion |
| Support SLA breach rate | Must not increase above 15% | Avoid generating demand operations cannot fulfill |
| Post-support CSAT | Must not fall below 4.2/5 | Protect service quality |

### Statistical Design

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Confidence level** | 95% | Standard |
| **Statistical power** | 80% | Standard |
| **Minimum detectable effect** | 20% relative | 8% -> 9.6% planning assumption |
| **Baseline conversion rate** | 8% planning assumption | Replace with observed pre-test baseline |
| **Required sample size** | Approx. 14,200 offer views per variant | Two-proportion estimate for 8.0% vs 9.6% |
| **Estimated daily traffic** | TBD | Requires eligible booking volume |
| **Required test duration** | TBD, minimum 14 days | Duration depends on daily eligible offer views |
| **Minimum test duration** | 14 days | Run at least 2 full business cycles |

**Decision Rules**

- **Ship:** Treatment improves primary metric by at least the MDE with p < 0.05 and no guardrail regression.
- **Iterate:** Treatment improves directionally but does not reach significance, or improves selection but creates clarity concerns.
- **Kill:** Treatment does not improve selection or harms booking completion, support SLA, or CSAT.

---

## Cohort Analysis Plan

### Cohort Definitions

| Cohort | Definition | Why It Matters |
|--------|------------|----------------|
| First-time ECC users | Customers selecting ECC for the first time in a calendar week | Measures onboarding and first service value |
| Repeat eligible customers | Customers with at least two eligible export bookings in 90 days | Measures repeat selection potential |
| Forwarder-managed bookings | Customers identified as freight forwarders or booking agents | Tests partner-friendly segment behavior |
| Time-sensitive bookings | Bookings created within threshold days of documentation/cargo cutoff | Tests highest-urgency segment |

### Retention Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| W4 repeat eligibility engagement | Customers who return to create another eligible export booking within 4 weeks | TBD |
| 90-day repeat selection rate | Customers who select ECC again within 90 days / customers with another eligible booking | 25% |
| Repeat CSAT | Average CSAT among repeat ECC users | >= 4.4/5 |

### Key Cohort Question

Do customers who receive first support action within 24 hours select Export Customs Clearances again more often than customers who receive late or unclear support?

---

## SQL Starter Queries

### Weekly North Star Metric

```sql
WITH selected AS (
  SELECT
    booking_id,
    customer_id,
    booking_completed_at
  FROM events
  WHERE event_name = 'booking_completed_with_ecc'
),
first_action AS (
  SELECT
    booking_id,
    MIN(event_time) AS first_action_at
  FROM events
  WHERE event_name = 'ecc_first_support_action_completed'
  GROUP BY booking_id
)
SELECT
  DATE_TRUNC(selected.booking_completed_at, WEEK) AS week,
  COUNT(DISTINCT selected.booking_id) AS clearance_supported_export_bookings
FROM selected
JOIN first_action USING (booking_id)
WHERE TIMESTAMP_DIFF(first_action.first_action_at, selected.booking_completed_at, HOUR) <= 24
GROUP BY 1
ORDER BY 1;
```

### Booking-Time Funnel

```sql
WITH funnel AS (
  SELECT
    booking_id,
    MAX(CASE WHEN event_name = 'export_booking_eligible_for_ecc' THEN 1 ELSE 0 END) AS eligible,
    MAX(CASE WHEN event_name = 'ecc_offer_viewed' THEN 1 ELSE 0 END) AS offer_viewed,
    MAX(CASE WHEN event_name = 'ecc_offer_details_opened' THEN 1 ELSE 0 END) AS details_opened,
    MAX(CASE WHEN event_name = 'ecc_service_selected' THEN 1 ELSE 0 END) AS service_selected,
    MAX(CASE WHEN event_name = 'booking_completed_with_ecc' THEN 1 ELSE 0 END) AS completed_with_ecc,
    MAX(CASE WHEN event_name = 'ecc_first_support_action_completed' THEN 1 ELSE 0 END) AS first_support_action
  FROM events
  WHERE event_time >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
  GROUP BY booking_id
)
SELECT
  COUNT(DISTINCT CASE WHEN eligible = 1 THEN booking_id END) AS eligible_bookings,
  COUNT(DISTINCT CASE WHEN offer_viewed = 1 THEN booking_id END) AS offer_views,
  COUNT(DISTINCT CASE WHEN details_opened = 1 THEN booking_id END) AS detail_opens,
  COUNT(DISTINCT CASE WHEN service_selected = 1 THEN booking_id END) AS selections,
  COUNT(DISTINCT CASE WHEN completed_with_ecc = 1 THEN booking_id END) AS completed_with_ecc,
  COUNT(DISTINCT CASE WHEN first_support_action = 1 THEN booking_id END) AS first_support_actions,
  ROUND(COUNT(DISTINCT CASE WHEN service_selected = 1 THEN booking_id END) * 1.0 /
        NULLIF(COUNT(DISTINCT CASE WHEN offer_viewed = 1 THEN booking_id END), 0), 4) AS offer_to_selection_rate
FROM funnel;
```

### Repeat Selection Cohort

```sql
WITH ecc_bookings AS (
  SELECT
    customer_id,
    booking_id,
    event_time AS selected_at,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY event_time) AS selection_number
  FROM events
  WHERE event_name = 'ecc_service_selected'
),
first_selection AS (
  SELECT
    customer_id,
    selected_at AS first_selected_at
  FROM ecc_bookings
  WHERE selection_number = 1
),
repeat_selection AS (
  SELECT DISTINCT
    first_selection.customer_id
  FROM first_selection
  JOIN ecc_bookings
    ON first_selection.customer_id = ecc_bookings.customer_id
   AND ecc_bookings.selected_at > first_selection.first_selected_at
   AND ecc_bookings.selected_at <= first_selection.first_selected_at + INTERVAL '90 days'
)
SELECT
  DATE_TRUNC(first_selected_at, WEEK) AS first_selection_week,
  COUNT(DISTINCT first_selection.customer_id) AS first_time_customers,
  COUNT(DISTINCT repeat_selection.customer_id) AS repeat_customers_90d,
  ROUND(COUNT(DISTINCT repeat_selection.customer_id) * 1.0 /
        COUNT(DISTINCT first_selection.customer_id), 4) AS repeat_selection_rate_90d
FROM first_selection
LEFT JOIN repeat_selection USING (customer_id)
GROUP BY 1
ORDER BY 1;
```

---

## Analytics Implementation Roadmap

| Priority | Action | Owner | Target Date | Success Metric |
|----------|--------|-------|-------------|----------------|
| 1 | Confirm canonical booking, VAS, customer, and support case identifiers | Product / Engineering / Data | 2026-06-07 | 100% event joinability in QA |
| 2 | Instrument booking eligibility, offer exposure, selection, and booking completion events | Engineering / Data | 2026-06-21 | 95% event capture accuracy |
| 3 | Instrument support case creation, assignment, first action, and completion events | Operations / Engineering | 2026-06-28 | 95% support workflow event coverage |
| 4 | Launch pilot dashboard for NSM, funnel, SLA, and guardrails | Data / Product | 2026-07-05 | Weekly dashboard reviewed by PM and Ops |
| 5 | Run ECC offer message A/B test after baseline is stable | Product / Data | TBD | Test reaches pre-defined sample size |

---

## Quality Checklist

- [x] North Star Metric captures customer value, not only revenue.
- [x] NSM has counter-metrics to prevent gaming.
- [x] A/B test hypothesis is written before data collection.
- [x] Sample size estimate is included before running.
- [x] Funnel steps are defined as specific event names.
- [x] Cohort analysis plan identifies retention and repeat-use behavior.
- [x] HEART framework maps at least two dimensions to specific metrics.
- [ ] Live baselines are available from production instrumentation.
